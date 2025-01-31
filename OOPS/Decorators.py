# Decorators --> A Decorator is a function that takes another function as an argument and returns a new function that modifies the behviour of the original function . The new function is ofenend refered to as decorated function 

# 1. Timing Function Execution : 
# Write a Decorator that measures the time a functtion takes to execute  

# import time 

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end - start} time")
#         return result
#     return wrapper


# @timer                          # This is Decorator --> Now whenever I call this function this will not directly call this will call only by passing from the timer function 
# def example_function(n):
#     time.sleep(n)
# example_function(2)


# 2 . Debugging Function calls 
# Create a decorator to print the function name and the values of its argument every time the function is called 

# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_value = ", ".join(str(arg) for arg in args)
#         kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
#         print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
#         return func(*args,**kwargs)
#     return wrapper

# @debug
# def greet(name,greeting = "Hello"):
#     print(f"{greeting} , {name}")

# greet("Vishal",greeting = "Hii")


# 3. Cache Return Values:
# Implement a decorator that caches the return values of a function , so that when it's called with the same arguments . the cached valur is returned instead of re-executing the function . 

import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def lon_running_function(a, b):
    time.sleep(4)
    return a + b

print(lon_running_function(2,3))
print(lon_running_function(2,3))  