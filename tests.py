# -*- coding: cp1251 -*-
import random
from tkinter import *
import datetime
import tkinter.ttk as ttk
import matplotlib
import matplotlib.pyplot as plt

if __name__ == '__main__':
    window = Tk()
    matplotlib.use('TkAgg')
    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=window)
    plot_widget = canvas.get_tk_widget()
    canvas.get_tk_widget()
    fig.clear()
    labels = ['Top10', 'Top9', 'Top8', 'Top7', 'Top6', 'Top5', 'Top4', 'Top3', 'Top2', 'Top1']
    plt.plot([random.randint(0, 10) for i in range(10)],
             [random.randint(0, 10) for i in range(10)]
             )  # х и у - списки значений абсциссы и ординаты
    plt.xticks(range(13), ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'])
    # print([(param, value) for param, value in plt.rcParams.items() if 'color' in param])
    # y = [257034, 260972, 343206, 362693, 413886, 521024, 670460, 722834, 748542, 1217913]
    plot_widget.grid(column=4, row=6)

    window.mainloop()  # Запуск главного цикла обработки событий

    # now = datetime.datetime.now()
    # print(datetime.datetime.now().strftime("%m/%d/%Y"))
    # print(datetime.datetime.now().strftime("%m/%d/%Y"))

    pass
