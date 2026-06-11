import tkinter as tk
from tkinter import ttk, messagebox


#Information on the prices, tickets, etc
Max_tickets = 5
child_price = 7.50
adult_price = 10.50
senior_price = 6.50
credit_surcharge = 0.05





def check_age(age):   
    '''
    This checks that the user has entered valid data.
    Age cannot be less than 12, or older than 114.
    '''

    try:
        new_age = int(age)
    except ValueError:
        messagebox.showerror("Input error", "Please enter an integer (I.e. An number without a decimal).")
        return -1

    if new_age < 12:
        messagebox.showerror("Error", "This customer is too young.")
        return -1
    elif new_age <16:
        return child_price
    elif new_age <65:
        return adult_price
    elif new_age< 115:
        return senior_price
    else:
        return -1
