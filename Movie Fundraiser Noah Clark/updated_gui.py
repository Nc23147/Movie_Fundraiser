import tkinter as tk
from tkinter import ttk, messagebox

#Colours
BG_COLOUR = "Orange"
FG_COLOUR = "white"
BORDER_COLOUR = "black"



#Main window
root = tk.Tk()
root.title ("Mini-movie Fundraiser")
root.geometry("400x300")
root.config(background=BG_COLOUR)

#Title
title_label = ttk.Label(root, text="Mini-Movie Fundraiser", font=("Verdana", 18, "bold"), foreground=FG_COLOUR)
title_label.grid(row=0, column=0, columnspan=2, pady=10)
title_label.config(background=BG_COLOUR)


#Name entry box
lbl_name = ttk.Label(root, text="Name:",font=("Verdana", 11 ,"bold") ,borderwidth=2, relief="solid")
lbl_name.grid(row=1, column=0, sticky= "w", padx=20, pady=20)
lbl_name.config(background=FG_COLOUR)

name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=1 , column= 1)


#Age entry box
lbl_age = ttk.Label(root, text="Age:", font=("Verdana", 11 ,"bold"),borderwidth=2, relief="solid")
lbl_age.grid(row=2, column=0, sticky = "w", padx= 20)
lbl_age.config(background=FG_COLOUR)

age_entry = ttk.Entry(root, width=25)
age_entry.grid(row=2, column=1)

#Payment Type
lbl_payment = ttk.Label(root, text="Payment Method:",font=("Verdana", 11 ,"bold"),borderwidth=1, relief="solid")
lbl_payment.grid(row=3, column=0, sticky = "w", padx= 20, pady=20)
lbl_payment.config(background=FG_COLOUR)

payment_method_box = ttk.Combobox(root, values=["Cash", "Credit"],font=("Verdana", 9 ,"bold"), state="readonly")
payment_method_box.grid(row = 3, column = 1)
payment_method_box.current(0)

#Create buttons
def create_frame(bg_color, border_color, border_width):
    '''This function will create a frame to give a black border around a button'''
    new_frame = tk.Frame(root, bg=bg_color, highlightbackground=border_color, highlightthickness=border_width, bd=0)
    return new_frame

#Submit button 
submit_frame = create_frame(BG_COLOUR, BORDER_COLOUR, 2)
submit_btn=tk.Button(
    submit_frame, 
    text= "Submit ticket",
    bg= BG_COLOUR,              #Background colour
    fg= FG_COLOUR,              #Text colour
    bd= 0, 
)
submit_btn.grid(row=9, column=1, pady=10)
submit_frame.grid(row=9, column=1,pady=10)

#finish button
finish_frame = create_frame(BG_COLOUR, BORDER_COLOUR, 2)
finish_btn = tk.Button(
    finish_frame, 
    text= "End program",
    bg= BG_COLOUR ,             #Background colour
    fg= FG_COLOUR,              #Text colour
    bd= 0,
)
finish_btn.grid(row=9, column=0, pady=10)
finish_frame.grid(row=9, column=0,pady=10)





root.mainloop()