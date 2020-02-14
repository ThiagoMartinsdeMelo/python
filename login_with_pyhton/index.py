from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

jan = Tk()
jan.title("System Login - Access Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

LeftFrame = Frame(jan, width=198, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=400, height=300, bg="MIDNIGHTBLUE",  relief="raise")
RightFrame.pack(side=RIGHT)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 14), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=126, y=106)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 14), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=126, y=156)

LoginButton = ttk.Button(RightFrame, text="Login", width="30")
LoginButton.place(x=80, y=200)

RegisterButton = ttk.Button(RightFrame, text="Register", width="30")
RegisterButton.place(x=80, y=234)

jan.mainloop()
