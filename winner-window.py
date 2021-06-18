import tkinter as tk
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


window = tk.Tk()
window.geometry("500x400")
window.title("winner screen")

value_inside = StringVar(window)
value_inside.set("Select your option")
bankOptions = ["ABSA", "FNB", "NedBank", "Standard Bank"]
variable = StringVar(window)
variable.set(bankOptions[0])


def clear():
    accountHolder_entry.delete(0, "end")
    accountNumber_entry.delete(0, "end")
    variable.set('')
    value_inside.set("")


def go():
    window.destroy()
    import converter


def send():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender = 'vandiemennahum@gmail.com'
    receivers =

bank_label = Label(window, text="Choose your bank:")
bank_label.place(x=50, y=30)
bank_select = OptionMenu(window, value_inside, variable, *bankOptions)
bank_select.place(x=260, y=30)
accountHolder_label = Label(window, text="Account holder name:")
accountHolder_label.place(x=30, y=80)
accountHolder_entry = Entry(window)
accountHolder_entry.place(x=260, y=80)
accountNumber_label = Label(window, text="Account Number:")
accountNumber_label.place(x=60, y=130)
accountNumber_entry = Entry(window)
accountNumber_entry.place(x=260, y=130)

convert = Button(window, text="Convert Money", command=go)
convert.place(x=280, y=350)
leave = Button(window, text="Exit", command=exit)
leave.place(x=430, y=350)
mail = Button(window, text="Send Email")
mail.place(x=20, y=350)
clear_entries = Button(window, text="Clear", command=clear)
clear_entries.place(x=150, y=350)

window.mainloop()
