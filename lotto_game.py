import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import sample
import datetime

date = datetime.datetime.now()

window = tk.Tk()
window.geometry("700x500")
window.title("Ithuba National Lottery:Lotto machine")
lotto_rand = sample(range(1, 49), 6)
lotto_rand.sort()
print(lotto_rand)

# Labels

lotto_lbl = Label(window, text="Choose your numbers")
lotto_lbl.place(x=250, y=20)
lottoNum_label = Label(window, text="Lotto Number Generator")
lottoNum_label.place(x=240, y=70)
results = Entry(window, width=20, height=20)
results.place(x=290, y=160)

# lotto number sets

lotto_num1 = Spinbox(window, width=3, from_=1, to=49)
lotto_num1.place(x=160, y=100)
lotto_num2 = Spinbox(window, width=3, from_=1, to=49)
lotto_num2.place(x=220, y=100)
lotto_num3 = Spinbox(window, width=3, from_=1, to=49)
lotto_num3.place(x=280, y=100)
lotto_num4 = Spinbox(window, width=3, from_=1, to=49)
lotto_num4.place(x=340, y=100)
lotto_num5 = Spinbox(window, width=3, from_=1, to=49)
lotto_num5.place(x=410, y=100)
lotto_num6 = Spinbox(window, width=3, from_=1, to=49)
lotto_num6.place(x=470, y=100)


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

play_button = Button(window, text="PLAY")
play_button.place(x=30, y=450)
playAgain_button = Button(window, text="Play Again", command=remove)
playAgain_button.place(x=100, y=450)
claim_button = Button(window, text="Claim Prize")
claim_button.place(x=300, y=450)
clear_button = Button(window, text="CLEAR", command=remove)
clear_button.place(x=540, y=450)
exit_button = Button(window, text="EXIT", command=exit)
exit_button.place(x=620, y=450)

window.mainloop()
