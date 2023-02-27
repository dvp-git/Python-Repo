# """ Iterable and dictionary unpacking"""
# def func(a, b, c, d, e, f):
#     print(a, b, c, d, e, f)


# func(1, *(2, 3), f=6, *(4, 5))


# func(*(1, 2), e=5, *(3, 4), f=6)


# func(1, **{'b': 2, 'c': 3}, d=4, **{'e': 5, 'f': 6})


# func(c=3, *(1, 2), **{'d': 4}, e=5,**{'f': 6})


"""
General Order of preferance:  positional-only --> then positional or keyword parameters -->  keyword-only ones.

def func_name(positional_only_parameters, /,
    positional_or_keyword_parameters, *,
    keyword_only_parameters):

# Samples:
def func_name(p1, p2, /, p_or_kw, *, kw):

def func_name(p1, p2=None, /, p_or_kw=None, *, kw):

def func_name(p1, p2=None, /, *, kw):

def func_name(p1, p2=None, /):

def func_name(p1, p2, /, p_or_kw):

def func_name(p1, p2, /):





"""

"""Variable Keyword arguments , default """
# def connect_(**options):
#     conn_ = {
#       'host' : options.get('host','129.0.0.1'),
#       'port' : options.get(4995)
#       }
#     print(conn_)
    
# connect_()

""" Variations of variable keyword arguments"""
# parameters.keyword.only.py
# def kwo(*a, c):
#     print(a, c)
# kwo(1, 2, 3, c=7)  # prints: (1, 2, 3) 7
# kwo(c=4)           # prints: () 4
# kwo(1, 2)  # breaks, invalid syntax, with the following error
# TypeError: kwo() missing 1 required keyword-only argument: 'c'



# def kwo2(a, b=42, *, c): # Everything after * is 'keyword ONLY'
#     print(a, b, c)
# kwo2(3, b=7, c=99)  # prints: 3 7 99
# kwo2(3, c=13)       # prints: 3 42 13
# kwo2(3, 23)  # breaks, invalid syntax, with the following error
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'


"""Conventional way *args is position only params, and **kwargs is keyword only parameters"""
# parameters.all.py
# def func(a, b, c=7, *args, **kwargs):
#     print('a, b, c:', a,b, c)
#     print('args:', args)
#     print('kwargs:', kwargs)
# func(1, 2, 3, 5, 7, 9, A='a', B='b')



""" Testing mutability lists and dictionaries: Retains entries of local scope if called again """
# def func(a=[], b={}):
#     print(a)
#     print(b)
#     print('#' * 12)
#     a.append(len(a))  # this will affect a's default value
#     b[len(a)] = len(a)  # and this will affect b's one

# func()
# func(a=[1, 2, 3], b={'B': 1})
# func()  


""" Display Fibonacci using Recursion upto limit"""
# def fib_print(limit,prev=0, current=1):  
#   # We need prev and current due to recursive nature
#   if current > limit :
#     return
#   else:
#     print(current,end=', ')
#     fib_print(limit,current,prev+current)

# print(fib_print(100))



""" Display all prime numbers up till n"""
# Logic check only if divisible by sqrt(n) because if not prime then n = a * b has :
# a = root(n) and b = root(n) OR a < root(n) , b > root(n) OR a> root(n) , b < root(n)
# Need to find if one of the factors is divisible by root(n) or items before root(n)  
# and if root(n) is non-prime < primelist, then check if n is only divisible by prime numbers less than root(n)
from math import sqrt, ceil
def get_primes(n):
    """Calculate a list of primes up to n (included). """
    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))  # division limit
        for prime in primelist:  # we try only the primes
            if prime > root:  # no need to check any further, we have already checked up for prime numbers till root(n)
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist

print(get_primes(15))