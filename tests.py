# -*- coding: cp1251 -*-
import random
from tkinter import *
import datetime
import tkinter.ttk as ttk
import matplotlib
import matplotlib.pyplot as plt
from time import *


# def next_load():
#     global state
#     print(state)
#     canvas.itemconfigure(loader[state], fill='orange')
#     canvas.itemconfigure(loader[state], outline='orange')
#     state = (state + 1) % 5
#     canvas.itemconfigure(loader[state], fill='blue')
#     canvas.itemconfigure(loader[state], outline='blue')
#     window.update()


if __name__ == '__main__':
    # print(datetime.datetime(year=2022, month=1, day=1))

    # window = Tk()
    # matplotlib.use('TkAgg')
    # fig = plt.figure()
    # canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=window)
    # plot_widget = canvas.get_tk_widget()
    # canvas.get_tk_widget()
    # fig.clear()
    # labels = ['Top10', 'Top9', 'Top8', 'Top7', 'Top6', 'Top5', 'Top4', 'Top3', 'Top2', 'Top1']
    # plt.plot([random.randint(0, 10) for i in range(10)],
    #          [random.randint(0, 10) for i in range(10)]
    #          )  # х и у - списки значений абсциссы и ординаты
    # plt.xticks(range(13), ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'])
    # print([(param, value) for param, value in plt.rcParams.items() if 'color' in param])
    # y = [257034, 260972, 343206, 362693, 413886, 521024, 670460, 722834, 748542, 1217913]
    # plot_widget.grid(column=4, row=6)

    # canvas = Canvas(window, width=200, height=20)
    # canvas = Canvas(window)
    # loader = []
    # d = 5
    # for i in range(4):
    #     loader.append(
    #         canvas.create_rectangle(d + 6 * d * i, d, 6 * d * i + 5 * d, 5 * d, fill="orange", outline='orange'))
    # canvas.itemconfigure(loader[0], fill='blue')
    # canvas.itemconfigure(loader[0], outline='blue')
    # canvas.grid(column=4, row=4)
    # window.update()
    # state = 0
    #
    # draw_currency_graph_btn = Button(window, text="Постро", command=next_load)
    # draw_currency_graph_btn.grid(column=2, row=2)
    # window.mainloop()  # Запуск главного цикла обработки событий

    # now = datetime.datetime.now()
    # print(datetime.datetime.now().strftime("%m/%d/%Y"))
    # print(datetime.datetime.now().strftime("%m/%d/%Y"))

    pass
