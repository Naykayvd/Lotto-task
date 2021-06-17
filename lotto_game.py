import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import sample
import datetime

counter = 1

date = datetime.datetime.now()

window = tk.Tk()
window.geometry("700x500")
window.title("Ithuba National Lottery:Lotto machine")

# Labels

lotto_lbl = Label(window, text="Choose your numbers")
lotto_lbl.place(x=250, y=20)
lottoNum_label = Label(window, text="Lotto Number Selector")
lottoNum_label.place(x=240, y=70)
lottoBalls1 = Entry(window)

# lotto number sets

lotto_num1 = Spinbox(window, from_=1, to=49)
lotto_num1.place(x=160, y=100, width=40, height=40)
lotto_num2 = Spinbox(window, from_=1, to=49)
lotto_num2.place(x=220, y=100, width=40, height=40)
lotto_num3 = Spinbox(window, from_=1, to=49)
lotto_num3.place(x=280, y=100, width=40, height=40)
lotto_num4 = Spinbox(window, from_=1, to=49)
lotto_num4.place(x=340, y=100, width=40, height=40)
lotto_num5 = Spinbox(window, from_=1, to=49)
lotto_num5.place(x=410, y=100, width=40, height=40)
lotto_num6 = Spinbox(window, from_=1, to=49)
lotto_num6.place(x=470, y=100, width=40, height=40)

nums = []
set01 = []
set02 = []
set03 = []
set01.sort()
set02.sort()
set03.sort()
result = set(set01), (set02), (set02).intersection(nums)


def generate():
    number = [i for i in range(1, 50)]
    random.shuffle(number)
    nums = number[:6]
    print(number)
    print(nums)

    try:
        lotto_nums = [int(lotto_num1.get()), int(lotto_num2.get()), int(lotto_num3.get()), int(lotto_num4.get()),
                      int(lotto_num5.get()), int(lotto_num6.get())]
        print(lotto_nums)

        for k in range(len(number)):
            if len(set01) < 6:
                set01.append(number[k])
            elif len(set01) == 6 and len(set02) < 6:
                set02.append(number[k])
            elif len(set02) == 6 and len(set03) < 6:
                set03.append(number[k])
    except:
        pass


def play():
    global counter
    if counter == 1:
        # game 1 use set01
        counter += 1
    elif counter == 2:
        # game 2 use set02
        counter += 1
    elif counter == 3:
        # game 3 use set03
        counter += 1


def remove():
    lotto_num1.delete(0, "end")
    lotto_num1.insert(1, 1)
    lotto_num2.delete(0, "end")
    lotto_num2.insert(1, 1)
    lotto_num3.delete(0, "end")
    lotto_num3.insert(1, 1)
    lotto_num4.delete(0, "end")
    lotto_num4.insert(1, 1)
    lotto_num5.delete(0, "end")
    lotto_num5.insert(1, 1)
    lotto_num6.delete(0, "end")
    lotto_num6.insert(1, 1)


# The buttons

play_button = Button(window, text="PLAY", command=generate)
play_button.place(x=30, y=450)
playAgain_button = Button(window, text="Play Again")
playAgain_button.place(x=100, y=450)
claim_button = Button(window, text="Claim Prize")
claim_button.place(x=300, y=450)
clear_button = Button(window, text="CLEAR", command=remove)
clear_button.place(x=540, y=450)
exit_button = Button(window, text="EXIT", command=exit)
exit_button.place(x=620, y=450)

generate()
window.mainloop()
