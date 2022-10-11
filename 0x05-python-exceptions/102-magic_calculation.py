#!/usr/bin/python3
def magic_calculation(a, b):
    """does exactly as provided bytecode
    args
        a: first arg
        b: second arg
    Return: result of the function if executed and None otherwise
    """
    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            result = a ** b
            result += result / i
        except 'Too far':
            result = a + b
            break
    return result
