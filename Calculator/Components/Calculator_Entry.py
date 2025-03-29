from tkinter import *

def result_input(root):
    r_input = Entry(root, font=("Arial", 24), bd=10, relief=FLAT, justify="left")
    r_input.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)
    return r_input