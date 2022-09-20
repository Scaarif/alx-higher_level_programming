#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
print(f"Last digit of {number} is ", end="")
if number < 0:
    num *= -1
    print(f"-{num % 10}", end="")
else:
    print(num % 10, end="")
if (num % 10) > 5:
    print(" and is greater than 5")
elif (num % 10) == 0:
    print(" and is 0")
elif (num % 10) < 6 and (num % 10) != 0:
    print(" and is less than 6 and not 0")
