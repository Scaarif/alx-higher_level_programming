#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operators = ['+', '-', '*', '/']
    fn = [add, sub, mul, div]
    # If no of args provided is less/more than 3 print error
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    # Check if operator provided (argv[2]) is implemented
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    for idx, op in enumerate(operators):
        if sys.argv[2] == op:
            print("{} {} {} = {}".format(a, op, b, fn[idx](a, b)))
            exit(0)
    # If the operator is not implemented: loop exhausts without returning
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
