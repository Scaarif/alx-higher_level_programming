#!/usr/bin/python3
def fizzbuzz():
    """ Prints the numbers 1 to 100 separated by space.
    For multiples of three, prints Fizz and five, Buzz
    For multiples of both five and three, Fizzbuzz """
    # For numbers between 0 and 101: 1 - 100
    for i in range(1, 101):
        # Determine if a number is a multiple of both 3 and 5
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz ", end="")
        # Determine if a number is a multiple of 3
        elif (i % 3) == 0:
            print("Fizz ", end="")
        # Determine if a number is a multiple of 5
        elif (i % 5) == 0:
            print("Buzz ", end="")
        # print the rest of the numbers
        else:
            print(f'{i} ', end="")
