import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import sample
import datetime

date = datetime.datetime.now()

window = tk.Tk()
window.geometry("700x700")
window.title("Ithuba National Lottery:Lotto machine")
lotto_rand = sample(range(1, 49), 6)
print(lotto_rand)

Lotto_Prizes = {"zero": 0, "one": 0, "two": 20.00, "three": 100.50, "four": 2384.00, "five": 8584.00,
                "six": 10000000.00}

def generate():
    try:
        number_sets = [int(set01box1.get()), int(set01box2.get()), int(set01box3.get()), int(set01box4.get()),
                       int(set01box5.get()), int(set01box6.get()), int(set02box1.get()), int(set02box2.get()),
                       int(set02box3.get()), int(set02box4.get()), int(set02box5.get()), int(set02box6.get()),
                       int(set03box1.get()), int(set03box2.get()), int(set03box3.get()), int(set03box4.get()),
                       int(set03box5.get()), int(set03box6.get())]
        print(number_sets)
        x = set(number_sets).intersection(lotto_rand)
        print(len(x))

        if len(x) == 0:
            messagebox.showinfo("Better luck next time", "Your numbers were: " + str(number_sets) + "\n"
                                   "The winning numbers are: " + str(lotto_rand) + "\n" +
                                   "You earned R0" + "\n" + str(date))
            messagebox.askretrycancel("Better luck next time", "Would you like to try again?")
        if len(x) == 1:
            messagebox.showinfo("Better luck next time", "Your numbers were: " + str(number_sets) + "\n"
                                "The winning numbers are: " + str(lotto_rand) + "\n" +
                                "You earned R0" + "\n" + str(date))
            messagebox.askretrycancel("Better luck next time", "Would you like to try again?")
        if len(x) == 2:
            messagebox.showinfo("At least you won something", "Your numbers were: " + str(number_sets) + "\n"
                                "The winning numbers are: " + str(lotto_rand) + "\n" +
                                "You earned R" + "\n" + str(date))
            messagebox.askretrycancel("At least you won something", "Would you like to try again?")
        if len(x) == 3:
            messagebox.showinfo("Wow that's not bad", "Your numbers were: " + str(number_sets) + "\n"
                                "The winning numbers are: " + str(lotto_rand) + "\n" +
                                "You earned R100.50" + "\n" str(date))
            messagebox.askretrycancel("Wow that's not bad", "Would you like to try again?")
        if len(x) == 4:
            messagebox.showinfo("DECENT!!", "Your numbers were: " + str(number_sets) + "\n"
                                "The winning numbers are: " + str(lotto_rand) + "\n" +
                                "You earned R2384.00" + "\n" str(date))
            messagebox.askretrycancel("DECENT!!", "Would you like to try again?")
        if len(x) == 5:
            messagebox.showinfo("DECENT!!", "Your numbers were: " + str(number_sets) + "\n"
                                "The winning numbers are: " + str(lotto_rand) + "\n" +
                                "You earned R8584.00" + "\n" str(date))
            messagebox.askretrycancel("DECENT!!", "Would you like to try again?")
        if len(x) == 6:
            messagebox.showinfo("Congratulations. You won the jackpot", "Your numbers were: " + str(number_sets) + "\n"
                                "The winning numbers are: " + str(lotto_rand) + "\n" +
                                "You earned R10000000.00" + "\n" str(date))
            messagebox.askretrycancel("WELL DONE!!!", "WOULD YOU LIKE TO PLAY AGAIN!!?")


# Labels

lotto_lbl = Label(window, text="Choose your numbers")
lotto_lbl.place(x=280, y=20)
set01_label = Label(window, text="Set 01")
set01_label.place(x=150, y=70)
set02_label = Label(window, text="Set 02")
set02_label.place(x=150, y=170)
set03_label = Label(window, text="set 03")
set03_label.place(x=150, y=270)

# set 01

set01box1 = Spinbox(window, width=3, from_=1, to=49)
set01box1.place(x=40, y=100)
set01box2 = Spinbox(window, width=3, from_=1, to=49)
set01box2.place(x=100, y=100)
set01box3 = Spinbox(window, width=3, from_=1, to=49)
set01box3.place(x=160, y=100)
set01box4 = Spinbox(window, width=3, from_=1, to=49)
set01box4.place(x=220, y=100)
set01box5 = Spinbox(window, width=3, from_=1, to=49)
set01box5.place(x=280, y=100)
set01box6 = Spinbox(window, width=3, from_=1, to=49)
set01box6.place(x=340, y=100)

# set 02

set02box1 = Spinbox(window, width=3, from_=1, to=49)
set02box1.place(x=40, y=200)
set02box2 = Spinbox(window, width=3, from_=1, to=49)
set02box2.place(x=100, y=200)
set02box3 = Spinbox(window, width=3, from_=1, to=49)
set02box3.place(x=160, y=200)
set02box4 = Spinbox(window, width=3, from_=1, to=49)
set02box4.place(x=220, y=200)
set02box5 = Spinbox(window, width=3, from_=1, to=49)
set02box5.place(x=280, y=200)
set02box6 = Spinbox(window, width=3, from_=1, to=49)
set02box6.place(x=340, y=200)

# set 03

set03box1 = Spinbox(window, width=3, from_=1, to=49)
set03box1.place(x=40, y=300)
set03box2 = Spinbox(window, width=3, from_=1, to=49)
set03box2.place(x=100, y=300)
set03box3 = Spinbox(window, width=3, from_=1, to=49)
set03box3.place(x=160, y=300)
set03box4 = Spinbox(window, width=3, from_=1, to=49)
set03box4.place(x=220, y=300)
set03box5 = Spinbox(window, width=3, from_=1, to=49)
set03box5.place(x=280, y=300)
set03box6 = Spinbox(window, width=3, from_=1, to=49)
set03box6.place(x=340, y=300)


def remove():
    set01box1.delete(0, "end")
    set01box1.insert(1, 1)
    set01box2.delete(0, "end")
    set01box2.insert(1, 1)
    set01box3.delete(0, "end")
    set01box3.insert(1, 1)
    set01box4.delete(0, "end")
    set01box4.insert(1, 1)
    set01box5.delete(0, "end")
    set01box5.insert(1, 1)
    set01box6.delete(0, "end")
    set01box6.insert(1, 1)
    set02box1.delete(0, "end")
    set02box1.insert(1, 1)
    set02box2.delete(0, "end")
    set02box2.insert(1, 1)
    set02box3.delete(0, "end")
    set02box3.insert(1, 1)
    set02box4.delete(0, "end")
    set02box4.insert(1, 1)
    set02box5.delete(0, "end")
    set02box5.insert(1, 1)
    set02box6.delete(0, "end")
    set02box6.insert(1, 1)
    set03box1.delete(0, "end")
    set03box1.insert(1, 1)
    set03box2.delete(0, "end")
    set03box2.insert(1, 1)
    set03box3.delete(0, "end")
    set03box3.insert(1, 1)
    set03box4.delete(0, "end")
    set03box4.insert(1, 1)
    set03box5.delete(0, "end")
    set03box5.insert(1, 1)
    set03box6.delete(0, "end")
    set03box6.insert(1, 1)


# The buttons

play_button = Button(window, text="PLAY", command=generate)
play_button.place(x=300, y=650)
clear_button = Button(window, text="CLEAR", command=remove)
clear_button.place(x=100, y=650)
exit_button = Button(window, text="EXIT", command=exit)
exit_button.place(x=500, y=650)

window.mainloop()
