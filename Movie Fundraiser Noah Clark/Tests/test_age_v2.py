import age_v2

def test_check_age():
    #arrange
    ERROR = -1
    child_price = 7.50
    adult_price = 10.50
    senior_price = 6.50
    #act  
    #invalid
    str_input = age_v2.check_age("XLII")
    decimal_input = age_v2.check_age("12.5")
    
    #boundary
    low_input = age_v2.check_age(11)
    hi_input = age_v2.check_age(115)
    
    #expected
    exp_inp_low = age_v2.check_age(12)
    exp_inp = age_v2.check_age(13)
    exp_adlt= age_v2.check_age(55)
    exp_bnd_hi = age_v2.check_age(113)
    exp_inp_hi = age_v2.check_age(114)

    #assert
    assert str_input == ERROR
    assert decimal_input == ERROR
    
    assert low_input == ERROR
    assert hi_input == ERROR

    assert exp_inp_low == child_price
    assert exp_inp == child_price
    assert exp_adlt == adult_price
    assert exp_bnd_hi == senior_price
    assert exp_inp_hi == senior_price

