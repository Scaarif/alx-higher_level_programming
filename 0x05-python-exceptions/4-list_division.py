#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists
    args:
        my_list_1: first list
        my_list_2: second list
        list_length: list length
    Return: the result of the division as a list
    """
    res = []
    for i in range(list_length):
        try:
            res.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            res.append(0)
            print('division by 0')
            continue
        except (TypeError, ValueError):
            res.append(0)
            print('wrong type')
            continue
        except IndexError:
            res.append(0)
            print('out of range')
        finally:  # could make the division a var and append it to res here
            pass  # that way I call append only once
    return res
