#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from random import randint
from tkinter import Tk, Label, Button, Entry, Toplevel, filedialog

def openfile(event):
    global people_list, label_filename, people_list_len
    filename = filedialog.askopenfilename()
    people_list = open(filename, "r").read().split("\n")
    people_list_len = len(people_list)
    del people_list[people_list_len-1]
    people_list_len = people_list_len -1
    label_filename["text"]=filename

def random_winners(event):
    global winners_list
    winners_list = []
    index_winner = randint(0, people_list_len-1)
    for i in range(int(winners_count.get())):
        winners_list = winners_list + [people_list[index_winner]]
        index = randint(0, people_list_len-1)
        while index_winner == index:
            index = randint(0, people_list_len-1)
        index_winner = index
             
    win = Toplevel()
    win.title("Список переможців")
    Label(win, text = "Переможці конкурсу:").grid(row=0, column=0, columnspan=2)
    win.update()
    row = 1
    for i in range(int(winners_count.get())):
        sleep(2)
        Label(win, text = str(i+1)+".", fg="red").grid(row=row, column=0)
        Label(win, text = winners_list[i], fg="red").grid(row=row, column=1)
        row = row+1
        win.update()
    Label(win, text = "Вітаємо!!!", font="14", fg="Blue").grid(row=row, column=0, columnspan=2)
    win.mainloop()
  
root = Tk()
root.title("Рандомайзер 3000")
label_1 = Label(root, text="Виберіть файл з іменами учасників конкурсу:")
label_1.grid(row=0, column=0, columnspan=2)

label_filename = Label(root, text="")
label_filename.grid(row=1, column=1)

bt_1 = Button(root, text="Вибрати")
bt_1.grid(row=1, column=0)
bt_1.bind("<Button-1>", openfile)

label_1 = Label(root, text="Вкажіть кількість переможців розіграшу:")
label_1.grid(row=2, column=0, columnspan=2)

winners_count = Entry(root)
winners_count.grid(row=3, column=0, columnspan=2)

label_1 = Label(root, text="Натисніть кнопку для запуску Рандомейзера:")
label_1.grid(row=4, column=0, columnspan=2)

bt_2 = Button(root, text="Визначити переможця")
bt_2.grid(row=5, column=0, columnspan=2)
bt_2.bind("<Button-1>", random_winners)

root.mainloop()