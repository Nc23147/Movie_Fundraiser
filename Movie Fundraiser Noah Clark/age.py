def check_age(age):   
    if isinstance(age, str) or isinstance(age, float):
        return "please enter an integer (ie: a number which does not have a decimal part)"
    elif age < 12:
        return "please enter an integer that is more than (or equal to) 12"
    elif age > 114:
        return "please enter an integer that is less than 115."
    
    return "thank you"


age=int(input("Please enter your age: "))
#check_age(age)
print(check_age(age))


