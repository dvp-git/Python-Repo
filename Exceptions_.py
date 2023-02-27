##############################################
""" Exceptions and Context Managers """
##############################################
""" Use raise Exception("Message ")


https://docs.python.org/3.9/library/exceptions.html#bltin-exceptions.

All exceptions even custom are to inherit from the Exception Class.

Read tracebacks from bottom to top.

try : handles exception. Try this block of code. Keep as  as short as possible

except : The kind of exception to be raised and handled if the try block catches an exception. Make the except clauses as specific as you can. 

else: Code to be executed if try block executes without any exception. 

finally (optional) : Clean up resources, Executed regardless of the outcome of try block.



The contextlib module: is the standard library provides a handy contextmanager decorator that takes a generator function and converts it into a context manager 


"""
# Ex:
def try_syntax(numerator, denominator): 
    try: 
        print(f'Attempting try block: {numerator}/{denominator}') 
        result = numerator / denominator 
    except ZeroDivisionError as zde: 
        print(f"Error {zde}") 
    else: 
        print('The result is:', result) 
        return result 
    finally: 
        print('Exiting ...') 
print(try_syntax(12, 4)) 
print(try_syntax(11, 0))

""" Catching many exceptions:
except (ZeroDivisionError, TypeError) as e:
    # Code to print error message

OR handle each one differently

except ZeroDivisionError:
    print("You tried to divide by zero!")
except TypeError as e:
    print(e)


"""
values = (2, 'sd')
try:
    q, r = divmod(*values)
except (ZeroDivisionError, TypeError) as e:
    print(type(e),e)

# >>> values = (2,0)
# >>> try:
# ...     q,r = divmod(*values)
# ... except (ZeroDivisionError, TypeError) as e:
# ...     print(type(e), e)
# ...
# <class 'ZeroDivisionError'> integer division or modulo by zero
# >>> values = (2,'sd')
# >>> try:
# ...     q,r = divmod(*values)
# ... except (ZeroDivisionError, TypeError) as e:
# ...     print(type(e), e)
# ...
# <class 'TypeError'> unsupported operand type(s) for divmod(): 'int' and 'str'

"""

Can also raise exceptions from within an except clause

try:   
    # some code here
except Error as e:
    raise DifferentError(*e.args)

"""
# values = ('asd',3)
# try:
#     q, r = divmod(*values)
# except TypeError as e:
#     raise NotImplemented(*e.args)


# If you wish to replace a built-in exception (or one from a third-party library) with your own custom exception

class NotFoundError(Exception):
    pass
vowels = {'a': 1, 'e': 5, 'i': 9, 'o': 15, 'u': 21}


# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyError: 'y'
# During handling of the above exception, another exception occurred:
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# __main__.NotFoundError: y

""" Error derved from Exception but message is from customr error:
except Actual error as e:
        raise CustomError from e"""

try:
    pos = vowels['y']
except KeyError as e:
    raise NotFoundError(*e.args) from e

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyError: 'y'
# The above exception was the direct cause of the following exception:
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# __main__.NotFoundError: y

""" Suppress original traceback using :  from None"""


#######################
# Context Managers
#######################

from decimal import Context, Decimal, getcontext, setcontext
one = Decimal("1")
three = Decimal("3")
orig_ctx = getcontext()
ctx = Context(prec=5)
setcontext(ctx)
print(ctx)
print(one / three)
setcontext(orig_ctx)
print(one / three)


orig_ctx = getcontext()
ctx = Context(prec=5)
setcontext(ctx)
try:
    print(ctx)
    print(one / three)
finally:
    setcontext(orig_ctx)
print(one / three)


from decimal import localcontext
with localcontext(Context(prec=5)) as ctx:
    print(ctx)
    print(one / three)
print(one / three)

"""
When managing resources we need to ensure to cleanup after exception occurs. We could use try/ finally each time, which gets cluttered.
Instead use the Context Managers : 

Creates Execution context : work with modified state , automatically perform any cleanup.

The with statement :  is used to enter a runtime context defined by a context manager

multiple context managers:  
Ex: with localcontext(Context(prec=5)), open("out.txt", "w") as out_f:
    out_f.write(f"{one} / {three} = {one / three}\n")

Examples:
Socket objects :  implement a low-level networking interface, can be used as context managers to automatically close network connections.
lock classes  :   used for synchronization in concurrent programming use the context manager protocol to automatically release locks.

"""


######################
# Context managers
######################
# __enter__ : called before entering context manager.
# __exit__ : called before exiting the context manager.

class MyContextManager():
    def __init__(self):
        print("MayContextManager {}".format(id(self)))

    def __enter__(self):
        print("Entering context manager...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # type, value, and traceback of the exception as arguments through these parameters. 
        # If no exception is raised, all three arguments will be None.
        print("exc_type={} exc_value={} exc_tracebak={}".format(exc_type, exc_val, exc_tb))
        print("Exiting context")
        return True

a = MyContextManager()

# with a as e:
#     print(id(a))
#     raise Exception("Exception inside 'with' context")
#     print("This line will never be reached")

# print("After with context")



## Contextlib modules @contextmanager decorator.
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Enter 'with' context")
    val = object()
    print(id(val))
    try:
        yield val
    except Exception as e:
        print("type(e)={} e={} traceback={}".format(type(e),e,e.__traceback__))
    finally:
        print("Exiting 'with' context")

print("About to enter 'with context")
with my_context_manager() as val:
    print("Inside with context")
    print(id(val))
    raise Exception ("Exception inside with context")
    print("This is not reached")
print("After with context")