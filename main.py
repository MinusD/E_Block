from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import xml.dom.minidom
import config


def get_data_from_cbr(date):
    answer = []
    response = urllib.request.urlopen("http://cbr.ru/scripts/XML_daily.asp?date_req=22/04/2022")
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


# dom = xml.dom.minidom.parse(response)  # Получение DOM структуры айла
# dom.normalize()
# nodeArray = dom.getElementsByTagName("TagName")  # Получение злементов с тегом
# for node in nodeArray:
# # Получение дочеpниx ³леентв
# childList = node.childNodes
# for child in childList:
#     print(child.nodeName)  # Получение имени узла
# print(child.childNodes[0].nodeValue)  # Получение значения

def clicked():
    pass


if __name__ == '__main__':
    # get_data_from_cbr(123)
    window = Tk()
    window.title(config.WINDOW_TITLE)
    window.geometry(config.WINDOW_SIZE)

    tab_control = ttk.Notebook(window)  # Виджет управления вкладками
    tab1 = ttk.Frame(tab_control)  # Виджет рамки (вкладка)
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text="Калькулятор валют")
    tab_control.add(tab2, text="Динамика курса")

    combo = ttk.Combobox(tab1)  # Создание комбобокса на первой вкладке, можно добавить аргументы, например ширину
    combo["values"] = ["раз", "два", "три"]
    combo.grid(column=0, row=0)  # Размещение в окне, указана позиция, можно указать отступы

    txt = Entry(tab1)  # Текстовое поле для ввода
    btn = Button(tab1, text="Действие", command=clicked)  # Кнопка, действие реализуется в функции clicked
    lb1 = Label(tab1, text="123")  # Надпись
    lb1.grid(column=1, row=2)
    # tab_control.add(tab1, txt)
    # Все объекты должны размещаться функцией grid
    # Существуют функции для программного получения значения текстового поля и изменения надписи

    tab_control.pack(expand=1, fill='both')  # Открытие первой вкладки
    window.mainloop()  # Запуск главного цикла обработки событий
