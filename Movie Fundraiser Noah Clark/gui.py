import tkinter as tk
from tkinter import ttk, messagebox

#main window
root = tk.Tk()
root.title ("Mini-movie Fundraiser")
root.geometry("300x300")

title_label =ttk.Label(root, text="mini-Movie Fundraiser", font=("Verdana", 18, "bold"))
title_label.grid (row=0, column=0, columnspan=2, pady=10)


root.mainloop()