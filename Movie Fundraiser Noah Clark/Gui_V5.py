import tkinter as tk
from tkinter import ttk, messagebox



#Colours
BG_COLOUR = "Orange"
FG_COLOUR = "white"
BORDER_COLOUR = "black"

#Variables
Max_tickets = 5
child_price = 7.50
adult_price = 10.50
senior_price = 6.50
credit_surcharge = 0.05
payment_types = ('Cash', 'Credit')
#Data lists 
all_names = []
all_ticket_costs = []
all_surcharges = []

tickets_sold = 0


#Functions
def check_age(age_string):   
    '''
    This checks that the user has entered valid data.
    Age cannot be less than 12, or older than 114.
    '''

    try:
        new_age = int(age_string)
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
    print(age)
    


    #If the name is empty shows an error
    if name == "":
        messagebox.showerror("Input Error", "Name connot be blank.")
        return
    elif name.isdigit():
        messagebox.showerror("Input Error", "Name cannot be a number")
        return
    else:
        print(name)
    ticket_price = check_age(age)
    
    if ticket_price == -1:
        return

    all_names.append(name)
    all_ticket_costs.append(ticket_price)

    if pay_method == payment_types[0]:
        all_surcharges.append(0)
    else:
        all_surcharges.append(ticket_price * credit_surcharge)
    
    name_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)
    payment_method_box.current(0)

from datetime import date

def end_program():
    total_tix_sold = len(all_names)
    total_profit = 0
    total_surcharge = 0
    total_paid = 0
    
    today = date.today()
    heading = make_statement(f"Mini Movie Fundraiser Ticket Data ({today})", "=")
    
    output = heading + "\n"
    output += "\nName       | Ticket Price | Surcharge    | Total     | Profit \n"
    output += "-" * 65 + "\n"

    for i in range(total_tix_sold):
        profit = 0
        total_surcharge += all_surcharges[i]
        
        individual_total = all_ticket_costs[i] + all_surcharges[i]
        total_paid += individual_total
        
        if all_ticket_costs[i] == 10.5:
            profit = 5.5
        elif all_ticket_costs[i] == 7.5:
            profit = 2.5
        elif all_ticket_costs[i] == 6.5:
            profit = 1.5
        
        total_profit += profit

        output += f"{all_names[i]:<10} {to_currency(all_ticket_costs[i]):<14} {to_currency(all_surcharges[i]):<14} {to_currency(individual_total):<11} {to_currency(profit):<10}\n"
    
    output += "\n" + "-" * 65 + "\n"
    output += f"Total Paid: {to_currency(total_paid)}\n"
    output += f"Total Profit: {to_currency(total_profit)}\n"
    
    save_to_file(output)
    print(output)


def make_statement(statement, decoration):
    return f"{decoration * 3} {statement} {decoration * 3}"

def to_currency(x):
    return "${:.2f}".format(x)

def save_to_file(output):
    file = open("movie_data.txt", "w")
    file.write(output)
    file.close()


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
    command=submit_ticket,
    text= "Submit ticket",
    bg= BG_COLOUR,              #Background colour
    fg= FG_COLOUR,              #Text colour
    bd= 0, 
)
submit_btn.grid(row=9, column=0)
submit_frame.grid(row=9, column=0,pady=20,padx=20)

#finish button
finish_frame = create_frame(BG_COLOUR, BORDER_COLOUR, 2)
finish_btn = tk.Button(
    finish_frame, 
    text= "End program",
    command= end_program,
    bg= BG_COLOUR ,             #Background colour
    fg= FG_COLOUR,              #Text colour
    bd= 0,
)
finish_btn.grid(row=9, column=1)
finish_frame.grid(row=9, column=1,pady=20,padx=20)








root.mainloop()