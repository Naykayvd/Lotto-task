import tkinter as tk
from tkinter import *
import requests

window = tk.Tk()
window.geometry("400x550")
window.title("Lotto currency converter")

value = IntVar()

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
information_json = information.json()

conversion_rate = information_json["conversion_rates"]

user_amount_lbl = Label(window, text="Enter amount(in ZAR)")
user_amount_lbl.place(x=145, y=10)
user_amount_ent = Entry(window, textvariable=value)
user_amount_ent.place(x=130, y=40)
converter = Label(window, text="Select currency")
converter.place(x=160, y=70)

convert = Listbox(window)
for x in conversion_rate.keys():
    convert.insert(END, str(x))
    convert.place(x=130, y=120)

convert_to_label = Label(window, text="Converted amount")
convert_to_label.place(x=145, y=305)


def change():
    num = float(user_amount_ent.get())
    print(information_json["conversion_rates"][convert.get(ACTIVE)])
    ans = num * information_json["conversion_rates"][convert.get(ACTIVE)]
    convert_to_label["text"] = ans


def get_rid():
    user_amount_ent.delete(0, "end")


conversion_btn = Button(window, text="convert", command=change)
conversion_btn.place(x=170, y=500)
get_out_btn = Button(window, text="EXIT!!", command=exit)
get_out_btn.place(x=320, y=500)
eraser_btn = Button(window, text="CLEAR!!", command=get_rid)
eraser_btn.place(x=20, y=500)

window.mainloop()
