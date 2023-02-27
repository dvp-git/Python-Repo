######################
""" DECORATORS """
######################
"""
Python decorators allow you to change the behavior of a function without modifying the function itself.

Decorators hide the function they are decorating. If I check the __name__ or __doc__ method we get an unexpected result.

# def my_decorator_func(func):

#     def wrapper_func():
#         # Do something before the function.
#         func()
#         # Do something after the function.
#     return wrapper_func

"""




# Examples:

# from time import time, sleep

# def f(sleep_time=0.1):
#     sleep(sleep_time)

# def measure(func,*args,**kwargs):
#     t = time()
#     func(*args,**kwargs)
#     print(f"{func.__name__} took {time() - t}")

# measure(f,0.3)
# measure(f)


# def measure(func):
#     # Wrapper function
#     def wrapper(*args, **kwargs):

#         # Do something before the function
#         t = time()

#         # Calling the function
#         func(*args,**kwargs)

#         # Do something after the function

#         print(f"{func.__name__} took {time() - t}")
#     return wrapper

# f = measure(f) # Decoration point f is reassiged to function called wrapper. 
# f(sleep_time=1)


""" Alternative way of decorators:"""
# @decorator_func
# def func(arg1, arg2, ..):
#     pass

"""Multiple decorators """
# func = deco1(deco2(func))

# is equivalent to the following:

# @deco1
# @deco2
# def func(arg1, arg2, ...):
#     pass

""" decorator factory : Decorator takes arguments"""
# def func(arg1, arg2, ...):
#     pass
# func = deco_arg(arg_a, arg_b)(func)

# # is equivalent to the following:

# @decoarg(arg_a, arg_b)
# def func(arg1, arg2, ...):
#     pass

""" Since we re-assign f to a wrapper, f's attributes are lost, i.e. f.__name__  , f.__doc__
Use functools @wraps to retain attributes 
"""

# from time import sleep
# from functools import wraps

# def measure(func):
#     @wraps(func)
#     def wrapper_func(*args, **kwargs):
#         t = time()
#         func(*args, **kwargs)
#         print(func.__name__,'took:',time() - t)
#     return wrapper_func

# @measure
# def f(sleep_for=0.8):
#     """ Functions which sleeps for sleep_for seconds"""
#     sleep(sleep_for)

# f(0.9)
# print(f.__name__, f.__dict__)  # if @wraps is not put output is wrapper_func None


""" Example of a 2 decorators """
# from time import sleep , time
# from functools import wraps


# def measure(func):
#     @wraps(func)
#     def wrapper_func(*args, **kwargs):
#         t = time()
#         result = func(*args, **kwargs)
#         print(func.__name__,'took:',time() - t)
#         return result
#     return wrapper_func


# def max_result(func):
#     @wraps(func)
#     def wrapper_func(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if result > 100:
#             print("Can't print , time exceeded")
#         return result
#     return wrapper_func

# # @measure
# # @max_result
# def cube(n):
#     return n * n * n

# cube = max_result(cube)
# cube = measure(cube)

# print(cube(4))

"""A decorator factory"""
# from functools import wraps
# def measure(threshold):
#     def my_decorator_wrapper(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if result > threshold:
#                 print(
#                     f'Result is too big ({result}). '
#                     f'Max allowed is {threshold}.'
#                 )
#             return result
#         return wrapper
#     return my_decorator_wrapper

# @measure(125)
# def cube(n):
#     return n ** 3
# print(cube(5))

