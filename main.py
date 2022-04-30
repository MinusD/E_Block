from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import xml.dom.minidom
import random
import config


def get_currency_list() -> list:
    currency_list = [config.RUBLE_SLUG]
    response = urllib.request.urlopen(config.CBR_URL)
    dom = xml.dom.minidom.parse(response)  # Получение DOM структуры айла
    dom.normalize()
    node_array = dom.getElementsByTagName("ValCurs")  # Получили список объектов валют
    for currency in node_array:  # Перебираем по валютам
        for data in currency.childNodes:
            currency_list.append(data.childNodes[3].childNodes[0].nodeValue)
    return sorted(currency_list) if config.SORT_CURRENCY_LIST else currency_list


def get_current_exchange_rate(currency: str) -> float:
    if currency == config.RUBLE_SLUG:
        return 1.0
    response = urllib.request.urlopen(config.CBR_URL)
    dom = xml.dom.minidom.parse(response)  # Получение DOM структуры айла
    dom.normalize()
    node_array = dom.getElementsByTagName("ValCurs")  # Получили список объектов валют
    for currency_data in node_array:  # Перебираем по валютам
        for data in currency_data.childNodes:
            if data.childNodes[3].childNodes[0].nodeValue == currency:
                return float(data.childNodes[4].childNodes[0].nodeValue.replace(',', '.')) / float(
                    data.childNodes[2].childNodes[0].nodeValue.replace(',', '.'))


def convert_currency_input_to_btn() -> None:
    try:
        value = float(currency_input.get().replace(',', '.'))
        convert_error_label.configure(fg='black')
        currency_from, currency_to = currency_combo_from.get(), currency_combo_to.get()
        if currency_from and currency_to:
            convert_error_label.configure(
                text=(1 / get_current_exchange_rate(currency_from)) * get_current_exchange_rate(currency_to) * value)
            # print(currency_from, '->', currency_to)
            # print((1 / get_current_exchange_rate(currency_from)) * get_current_exchange_rate(currency_to))
            # print('======')
        else:
            convert_error_label.configure(fg='red')
            convert_error_label.configure(text=config.NO_END_CURRENCY_SELECTED_ERROR)
    except ValueError:
        convert_error_label.configure(fg='red')
        convert_error_label.configure(text=config.NOT_NUMERIC_VALUE_ERROR)
    # if value.isdigit():
    #     convert_error_label.configure(fg='black')
    # else:

    # sleep(1000)
    # convert_error_label.configure(fg='black')


def get_data_from_cbr(date):
    answer = []
    response = urllib.request.urlopen("http://cbr.ru/scripts/XML_daily.asp")
    dom = xml.dom.minidom.parse(response)  # Получение DOM структуры айла
    dom.normalize()
    node_array = dom.getElementsByTagName("ValCurs")  # Получили список объектов валют
    for currency in node_array:  # Перебираем по валютам
        for data in currency.childNodes:
            tmp = []
            for n in data.childNodes:
                tmp.append(n.childNodes[0].nodeValue)
            answer.append(tmp)
    print(answer)


if __name__ == '__main__':
    get_currency_list()
    window = Tk()
    # window.option_add("*Font", "courier 8")
    # window.option_add("*Font", "default_font")
    window.title(config.WINDOW_TITLE)
    window.geometry(config.WINDOW_SIZE)

    tab_control = ttk.Notebook(window)  # Виджет управления вкладками
    tab1 = ttk.Frame(tab_control)  # Виджет рамки (вкладка)
    tab2 = ttk.Frame(tab_control)

    # Вкладки приложения
    tab_control.add(tab1, text="Калькулятор валют")
    tab_control.add(tab2, text="Динамика курса")

    # Селектор выбора валюты (ИЗ)
    currency_combo_from = ttk.Combobox(tab1, state="readonly")
    currency_combo_from['values'] = get_currency_list()
    currency_combo_from.current(21 if config.SORT_CURRENCY_LIST else 0)  # В любом случае первая валюта - рубль
    currency_combo_from.grid(column=1, row=1, padx=config.PADX, pady=config.PADY)

    # Селектор выбора валюты (В)
    currency_combo_to = ttk.Combobox(tab1, state="readonly")
    currency_combo_to['values'] = get_currency_list()
    if config.RANDOM_START_CURRENCY:
        currency_combo_to.current(random.randint(0, len(currency_combo_to['values']) - 1))
    currency_combo_to.grid(column=1, row=2, padx=config.PADX, pady=config.PADY)

    # Поле ввода
    entryText = StringVar()
    currency_input = Entry(tab1, textvariable=entryText)
    entryText.set("1")
    currency_input.grid(column=2, row=1, padx=config.PADX, pady=config.PADY)
    currency_input.focus()

    # Кнопка конвертирования
    currency_convert_btn = Button(tab1, text="Конвертировать", command=convert_currency_input_to_btn)
    currency_convert_btn.grid(column=3, row=1, padx=config.PADX, pady=config.PADY)

    # Лайбел вывода конвертации/ошибки
    convert_error_label = Label(tab1, text="")  # Надпись
    convert_error_label.grid(column=2, row=2, padx=config.PADX, pady=config.PADY)

    # combo = ttk.Combobox(tab1)  # Создание комбобокса на первой вкладке, можно добавить аргументы, например ширину
    # combo["values"] = ["раз", "два", "три"]
    # print(combo["values"].size())
    # combo.grid(column=0, row=0)  # Размещение в окне, указана позиция, можно указать отступы

    # txt = Entry(tab1)  # Текстовое поле для ввода
    # btn = Button(tab1, text="Действие", command=clicked)  # Кнопка, действие реализуется в функции clicked
    # lb1 = Label(tab1, text="123")  # Надпись
    # lb1.grid(column=1, row=2)
    # tab_control.add(tab1, txt)
    # Все объекты должны размещаться функцией grid
    # Существуют функции для программного получения значения текстового поля и изменения надписи

    tab_control.pack(expand=1, fill='both')  # Открытие первой вкладки
    window.mainloop()  # Запуск главного цикла обработки событий
