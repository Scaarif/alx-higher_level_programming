#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int
roman_number = "XII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = 12
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "MMCDXXI" # 2000 + 400 + 20 + 1 = 2421
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = ""
print("{} = {}".format(roman_number, roman_to_int(roman_number)))