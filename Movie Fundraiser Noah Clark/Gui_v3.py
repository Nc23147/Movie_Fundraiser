import tkinter as tk
from tkinter import ttk, messagebox

#Main window
root = tk.Tk()
root.title ("Mini-movie Fundraiser")
root.geometry("400x300")

#Information on the prices, tickets, etc
Max_tickets = 5
child_price = 7.50
adult_price = 10.50
senior_price = 6.50
credit_surcharge = 0.05

#Data lists 
all_names = []
all_ticket_costs = []
all__surcharges = []

tickets_sold = 0
payment_types = ('Cash', 'Credit')

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
    else:
        return senior_price

def submit_ticket():
    name= name_entry.get().strip()
    pay_method = payment_method_box.get()
    print(pay_method)
    age = age_entry.get().strip()
    


    #If the name is empty shows an error
    if name == "":
        messagebox.showerror("Input Error", "Name connot be blank.")
        return
    else:
        print(name)
    ticket_price = check_age(age)
    
    all_names.append(name)
    all_ticket_costs.append(ticket_price)

    if pay_method == payment_types[0]:
        all__surcharges.append(0)
    else:
        all__surcharges.append(credit_surcharge)

title_label =ttk.Label(root, text="Mini-Movie Fundraiser", font=("Verdana", 18, "bold"))
title_label.grid (row=0, column=0, columnspan=2, pady=10)

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky = "e")
name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=1 , column= 1)

ttk.Label(root, text="age:").grid(row=2, column=0, sticky = "e")
age_entry = ttk.Entry(root, width=15)
age_entry.grid(row=2 , column= 1)

ttk.Label(root, text="Payment method: ").grid(row = 3,column=0, sticky = "e" )
payment_method_box = ttk.Combobox(root, values=["Cash", "Credit"], state="readonly")
payment_method_box.grid(row = 3, column = 1)
payment_method_box.current(0)

submit_btn=ttk.Button(root, text="Submit Ticket", command= submit_ticket)
submit_btn.grid(row = 4, column = 0, pady = 10)

finish_btn=ttk.Button(root, text="Finish early")
finish_btn.grid(row = 4, column = 1, pady = 10)

root.mainloop()