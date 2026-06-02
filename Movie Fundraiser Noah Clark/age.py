def get_age(age):   
    if isinstance(age, str) or isinstance(age, float):
        return "please enter an integer (ie: a number which does not have a decimal part)"
    elif age < 12:
        return "please enter an integer that is more than (or equal to) 12"
    elif age < 114:
        return "please enter an interger that is less than 115."
    return "thank you"
       
    pass