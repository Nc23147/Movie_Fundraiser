import age

def test_check_age():
    #arrange
    expected_err_invalid = "please enter an integer (ie: a number which does not have a decimal part)"
    expected_err_bound_low = "please enter an integer that is more than (or equal to) 12"
    expected_err_bound_high = "please enter an interger that is less than 115."
    expected_input = "thank you"


    #act 
 
    #invalid
    str_input = age.check_age("XLII")
    flt_input = age.check_age(12.5)
    
    #boundary
    low_input = age.check_age(11)
    hi_input = age.check_age(115)
    
    #expected
    exp_inp_low = age.check_age(12)
    exp_inp = age.check_age(13)
    #exp_bnd_hi = age.check_age(113)
    #exp_inp_hi = age.check_age(114)

    #assert
    assert str_input == expected_err_invalid
    assert flt_input == expected_err_invalid
    
    assert low_input == expected_err_bound_low
    assert hi_input == expected_err_bound_high

    assert exp_inp == expected_input
    assert exp_inp_low == expected_input