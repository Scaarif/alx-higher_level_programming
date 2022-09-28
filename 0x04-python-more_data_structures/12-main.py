#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "MMCDXXI" # 2000 + 400 + 20 + 1 = 2421
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "CCXLVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "XXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "DCCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "XL"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "XC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "C"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))