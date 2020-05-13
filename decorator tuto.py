# -*- coding: utf-8 -*-
 


###############doc string
from functools import wraps    
def print_funtion_data(function):     #decorator fn
    @wraps(function):
        def wrapper(*args, **kwargs)
        print("this is a good  wrapper{function__name__}")
        return any_function(*args, **kwargs)
    print(f"{function.__doc__}")
    return function((*args, **kwargs))
    return wrapper

@print_funtion_data
def add(a,b):
    '''this is add fn'''  ###doc string
    return  a + b


print(add.__doc__)

  