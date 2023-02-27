# Set comprehensions
from math import factorial

# General form  : {expr(item) for item in iterable}
# No duplicates , also sets are unordered unlike lists since they remove duplicates

f = {factorial(x) for x in range(20)}  # the Factorials upto 20
f_length = {len(str(factorial(x))) for x in range(20)}  # Length of the factorials , no duploicates
print(f)
print(f_length)
