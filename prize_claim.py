import smtplib
import tkinter as tk
from email import encoders
from email.mime.base import MIMEBase
from tkinter import *
from tkinter import messagebox

import email_validator

window = tk.Tk()
window.geometry("500x400")
window.title("winner screen")

value_inside = StringVar(window)
value_inside.set("Select your bank")
bankOptions = ["ABSA", "FNB", "NedBank", "Standard Bank"]
variable = StringVar(window)
variable.set(bankOptions[0])


def send():
    try:
        user_email = email_entry.get()
        valid = email_validator.validate_email(user_email)
        user_email = valid.email

        s = smtplib.SMTP('smtp.gmail.com', 587)
        sender = "nahvandiemen@gmail.com"
        receiver = [email_entry.get()]
        password = "n@#umvd98"
        s.starttls()
        s.login(sender, password)
        message = str(accountHolder_entry.get()) + "\n" + str(accountNumber_entry.get())
        message = message + str(bank_select.cget(bankOptions))
        s.sendmail(sender, receiver, message)
        filename = "results.txt"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Your results", f"attachment; filename = {filename}")
        print("email sent")
    except email_validator.EmailNotValidError:
        messagebox.showerror("Email Verification", "Please fill in a proper email address")
    finally:
        print("email sent")
        messagebox.showinfo("Email Sent", "Please check your email")


def clear():
    accountHolder_entry.delete(0, "end")
    accountNumber_entry.delete(0, "end")
    email_entry.delete(0, "end")
    variable.set('')
    value_inside.set("")


def go():
    window.destroy()
    import converter


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
email_entry_label = Label(window, text="Enter your email:")
email_entry_label.place(x=60, y=180)
email_entry = Entry(window)
email_entry.place(x=260, y=180)

convert = Button(window, text="Convert Money", command=go)
convert.place(x=280, y=350)
leave = Button(window, text="Exit", command=exit)
leave.place(x=430, y=350)
mail = Button(window, text="Send Email", command=send)
mail.place(x=20, y=350)
clear_entries = Button(window, text="Clear", command=clear)
clear_entries.place(x=150, y=350)

window.mainloop()
