from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import xml.dom.minidom
import random
import datetime
import re
import matplotlib
import matplotlib.pyplot as plt
import config


def get_currency_list(with_ruble: bool = True) -> list:
    currency_list = [config.RUBLE_SLUG] if with_ruble else []
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
        convert_out_label.configure(fg='black')
        currency_from = currency_combo_from.get()
        currency_to = currency_combo_to.get()
        if currency_from and currency_to:
            convert_out_label.configure(
                text=(1 / get_current_exchange_rate(currency_from)) * get_current_exchange_rate(currency_to) * value)
            # print(currency_from, '->', currency_to)
            # print((1 / get_current_exchange_rate(currency_from)) * get_current_exchange_rate(currency_to))
            # print('======')
        else:
            convert_out_label.configure(fg='red')
            convert_out_label.configure(text=config.NO_END_CURRENCY_SELECTED_ERROR)
    except ValueError:
        convert_out_label.configure(fg='red')
        convert_out_label.configure(text=config.NOT_NUMERIC_VALUE_ERROR)


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


def draw_currency_graph() -> None:
    pass


def date_to_dot_format(time) -> str:
    return str(time.day) + '.' + str(time.month) + '.' + str(time.year)


def change_selection_period() -> None:
    now = datetime.datetime.now()
    pr = radio_period_state.get()
    a = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']
    data = []
    delta = datetime.timedelta(days=1)
    if pr == 1:
        now -= 6 * delta
        for i in range(3):
            data.append(str(now.strftime('%d.%m.%Y') + '-' + (now + 6 * delta).strftime('%d.%m.%Y')))
            now -= 7 * delta
    elif pr == 2:
        print(now.month)
        for i in range(3):
            data.append(a[now.month % 12 - 1] + ' ' + str(now.year))
            now -= 30*delta

    period_combo['values'] = data
    period_combo.current(0)
    # print(datetime)
    # print(datetime.date.today())
    # print(radio_period_state.get())


if __name__ == '__main__':

    """
    Создание окна и вкладок
    """

    window = Tk()
    # window.option_add("*Font", "courier 8")
    # window.option_add("*Font", "default_font")
    window.title(config.WINDOW_TITLE)
    if config.WINDOW_SIZE:
        window.geometry(config.WINDOW_SIZE)

    tab_control = ttk.Notebook(window)  # Виджет управления вкладками
    tab1 = ttk.Frame(tab_control)  # Виджет рамки (вкладка)
    tab2 = ttk.Frame(tab_control)

    # Вкладки приложения

    tab_control.add(tab2, text="Динамика курса")
    tab_control.add(tab1, text="Калькулятор валют")
    # tab_control.enable_traversal()

    """
    Вкладка - Калькулятор валют
    """

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
    if config.SET_INITIAL_VALUE:
        entryText.set(config.SET_INITIAL_VALUE)
    currency_input.grid(column=2, row=1, padx=config.PADX, pady=config.PADY)
    currency_input.focus()

    # Кнопка конвертирования
    currency_convert_btn = Button(tab1, text="Конвертировать", command=convert_currency_input_to_btn)
    currency_convert_btn.grid(column=3, row=1, padx=config.PADX, pady=config.PADY)

    # Лайбел вывода конвертации/ошибки
    convert_out_label = Label(tab1, text="")
    convert_out_label.grid(column=2, row=2, padx=config.PADX, pady=config.PADY)

    """
    Вкладка - Динамика курса 
    """

    # Лайбел 'Валюта'
    currency_static = Label(tab2, text="Валюта")
    currency_static.grid(column=1, row=1, padx=config.PADX)

    # Лайбел 'Период'
    period_static = Label(tab2, text="Период")
    period_static.grid(column=2, row=1, padx=config.PADX)

    # Лайбел 'Выбор периода'
    select_period_static = Label(tab2, text="Выбор периода")
    select_period_static.grid(column=3, row=1, padx=config.PADX)

    # Селектор выбора валюты для построения графика
    currency_combo_graf = ttk.Combobox(tab2, state="readonly")
    currency_combo_graf['values'] = get_currency_list(False)
    currency_combo_graf.current(
        random.randint(0, len(currency_combo_to['values']) - 1) if config.RANDOM_CURRENCY else 0)
    currency_combo_graf.grid(column=1, row=2, padx=config.PADX, pady=config.PADY)

    # Селектор выбора валюты для построения графика
    period_combo = ttk.Combobox(tab2, state="readonly")
    period_combo.grid(column=3, row=2, padx=config.PADX, pady=config.PADY)

    # Радио длительности периода
    radio_period_state = IntVar()
    radio_period_state.set(1)
    change_selection_period()

    radio_period_1 = Radiobutton(tab2, text='Неделя', value=1, variable=radio_period_state,
                                 command=change_selection_period)
    radio_period_2 = Radiobutton(tab2, text='Месяц', value=2, variable=radio_period_state,
                                 command=change_selection_period)
    radio_period_3 = Radiobutton(tab2, text='Квартал', value=3, variable=radio_period_state,
                                 command=change_selection_period)
    radio_period_4 = Radiobutton(tab2, text='Год', value=4, variable=radio_period_state,
                                 command=change_selection_period)

    radio_period_1.grid(column=2, row=2)
    radio_period_2.grid(column=2, row=3)
    radio_period_3.grid(column=2, row=4)
    radio_period_4.grid(column=2, row=5)

    # matplotlib.use('TkAgg')
    # fig = plt.figure()
    # canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
    # plot_widget = canvas.get_tk_widget()
    # canvas.get_tk_widget()
    # fig.clear()
    # plt.plot(100, 100)  # х и у - списки значений абсциссы и ординаты
    # plt.grid()
    # plot_widget.grid(row=0, column=0)

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
