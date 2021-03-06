import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import *
from playsound import playsound
import email_validator

date = datetime.now()

window = tk.Tk()
window.geometry("460x360")
window.title("Ithuba National Lottery Login")


def erase():
    playsound("beep_beep.mp3")
    name_entry.delete(0, "end")
    email_entry.delete(0, "end")
    ID_entry.delete(0, "end")


def check():
    try:
        user_email = email_entry.get()
        valid = email_validator.validate_email(user_email)
        user_email = valid.email
        
        user_id = ID_entry.get()
        year = user_id[:2]
        playerID = (user_id[6:13])

        if year >= "22":
            year = "19" + year
        else:
            year = "20" + year
        month = user_id[2:4]
        day = user_id[4:6]
        today = date.today()

        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))

        if len(user_id) != 13:
            messagebox.showerror("Error", "Please enter valid ID number")
            playsound('beep_beep.mp3')
        elif len(user_id) == 0:
            messagebox.showwarning("Warning", "Please fill out the ID form")
            playsound('beep_beep.mp3')
        elif age >= 18:
            messagebox.showinfo("Welcome", "Let's Play" + "\n" + "\n" + "Your player ID is " + str(playerID))
            playsound('beep_beep.mp3')
            window.destroy()
            import lotto_game
        else:
            age = 18 - age
            messagebox.showerror("Warning", "You are too young to play. Please try again in " + str(age) + " years")
    except email_validator.EmailNotValidError:
        messagebox.showerror("Email Verification", "Please fill in a proper email address")


name_label = Label(window, text="Name:")
name_label.place(x=100, y=50)
name_entry = Entry(window)
name_entry.place(x=150, y=50)
email_label = Label(window, text="Email:")
email_label.place(x=100, y=100)
email_entry = Entry(window)
email_entry.place(x=150, y=100)
ID_label = Label(window, text="ID:")
ID_label.place(x=123, y=150)
ID_entry = Entry(window)
ID_entry.place(x=150, y=150)

name = name_entry.get()
email = email_entry.get()
ID = ID_entry.get()

enter_btn = Button(window, text="Validate", command=check)
enter_btn.place(x=50, y=250)
clear_btn = Button(window, text="Clear", command=erase)
clear_btn.place(x=200, y=250)
exit_btn = Button(window, text="Exit", command=exit)
exit_btn.place(x=330, y=250)

window.mainloop()
