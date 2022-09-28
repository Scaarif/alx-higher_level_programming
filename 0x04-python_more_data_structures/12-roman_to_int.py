#!/usr/bin/python3
def thousands(r_str):
    """ return number of m's in the str_ing """
    ms = 0
    i = 0
    if r_str[0] == 'M':
        while i < len(r_str):
            if r_str[i] == 'M' and ms <= 3:
                ms += 1
            else:
                break
            i += 1
    return ms


def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer
    Description:
        the number will be between 1 and 3999
    Args:
        roman_string: the roman numeral
    Returns:
        the integer equivalent of a roman numeral
    """
    # the value starts from left to right so...
    # given 2,421 = MMCDXXI = MM + CD + XX + I
    # if a str__ing starts with M, its in the thousands
    if isinstance(roman_string, str) and len(roman_string):
        str_ = roman_string
    else:
        return 0
    len_ = len(roman_string)
    # make all this a dictionary
    num = 0
    i = 0
    ms = 0
    cs = 0
    cd = 0
    cm = 0
    dc = 0
    xs = 0
    Is = 0
    xc = 0
    lx = 0
    xl = 0
    vi = 0
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    # deal with thousands
    if str_[0] == 'M':
        ms = thousands(str_)
        i += ms  # steps into the str_ing, str_
    num += ms * 1000
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    # deal with hundreds (1-400, 900 and 500-800)
    if i < len_ and str_[i] == 'C':
        cs += 1
        i += 1
        while i < len_ and str_[i]:
            if str_[i] == 'C' and cs <= 3:
                cs += 1
            elif str_[i] == 'D':
                cs -= 1
                cd += 1
                i += 1
                break
            elif str_[i] == 'M':
                cs -= 1
                cm += 1
                i += 1
                break
            else:
                break
            i += 1
    num += (cs * 100) + (cd * 400) + (cm * 900)
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    if i < len_ and str_[i] == 'D':
        i += 1
        num += 500
        while i < len_ and str_[i]:
            if str_[i] == 'C' and dc <= 3:
                dc += 1
            else:
                break
            i += 1
    num += dc * 100
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    # deal with ints less 100
    if i < len_ and str_[i] == 'X':
        i += 1
        xs += 1
        while i < len_ and str_[i]:
            if str_[i] == 'X' and xs <= 3:
                xs += 1
            elif str_[i] == 'C':
                xs -= 1
                xc += 1  # 90
            elif str_[i] == 'L':
                xs -= 1
                xl += 1
            else:
                break
            i += 1
    num += (xl * 40) + (xs * 10) + (xc * 90)
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    if i < len_ and str_[i] == 'L':
        i += 1
        num += 50
        while i < len_ and str_[i]:
            if str_[i] == 'X' and lx <= 3:
                lx += 1
            else:
                break
            i += 1
    num += lx * 10
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    # deal with ints less than 10
    if i < len_ and str_[i] == 'I':
        Is += 1
        i += 1
        while i < len_ and str_[i]:
            if str_[i] == 'I' and Is <= 3:
                Is += 1
            elif str_[i] == 'X':
                Is -= 1
                num += 9
            elif str_[i] == 'V':
                Is -= 1
                num += 4
            else:
                break
            i += 1
    num += Is * 1
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    if i < len_ and str_[i] == 'V':
        i += 1
        num += 5
        while i < len_ and str_[i]:
            if str_[i] == 'I' and vi <= 3:
                vi += 1
            else:
                break
            i += 1
    num += vi * 1
    # print("at str_: {} and i: {} where num is {}".format(str_[i:], i, num))
    return num
