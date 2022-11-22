'''  An *args and *kwargs reminder/ review module '''

# a function that accepts a variable number of arguments
def my_func(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

# define main
if __name__ == '__main__':
    a_dict = { 'name': "Best", 'age': 89 }
    
    # should print out the whole dict as a single arg
    my_func(a_dict)
    # should resolve each k-v pair as an arg (arg will be the key?)
    my_func(*a_dict)
    # should resolve each k-v pair as an kwarg
    my_func(**a_dict)

