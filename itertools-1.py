# Demonstration of itertools

from filtering_predicates import is_prime
from itertools import islice, count

# All 10 prime numbers
Iteration = islice((x for x in count() if is_prime(x)),10)  # islice((x for x in count() if is_prime(x)),10) infinite sequence of prime numbers for 10 numbers is the limit

for i in Iteration:
    print(i)

# Sum of all primes uptill 1000
print(sum(islice((x for x in count() if is_prime(x)),10)))  # If you pass Iteration here, answer will be 0 since the Iteration is already done. SO we have to pass the expression again.


sunday  = [12,14,16,18]
monday = [13,17,19,20]


# # Calculatin the average using Tuple Unpacking
# for sun,mon in zip(sunday,monday):
#     print("Average temp =",(sun+mon)/2)
#
#
# # Can be extended to any number of elements
# tuesday = [12,46,78,31]
# for temps in zip(sunday,monday,tuesday):
#     print("min ={:4.1f}, max = {:4.1f} , average = {:4.1f}".format(min(temps),max(temps),sum(temps)/len(temps)))

"""
itertools.count(start=0, step=1)
Make an iterator that returns evenly spaced values starting with number start. Often used as an argument to map() to generate consecutive data points. Also, used with zip() to add sequence numbers. Roughly equivalent to:

def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
When counting with floating point numbers, better accuracy can sometimes be achieved by substituting multiplicative code such as: (start + step * i for i in count()).



itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])
Make an iterator that returns selected elements from the iterable. If start is non-zero, then elements from the iterable are skipped until start is reached. Afterward, elements are returned consecutively unless step is set higher than one which results in items being skipped. If stop is None, then iteration continues until the iterator is exhausted, if at all; otherwise, it stops at the specified position. Unlike regular slicing, islice() does not support negative values for start, stop, or step. Can be used to extract related fields from data where the internal structure has been flattened (for example, a multi-line report may list a name field on every third line). Roughly equivalent to:

def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    start, stop, step = s.start or 0, s.stop or sys.maxsize, s.step or 1
    it = iter(range(start, stop, step))
    try:
        nexti = next(it)
    except StopIteration:
        # Consume *iterable* up to the *start* position.
        for i, element in zip(range(start), iterable):
            pass
        return
    try:
        for i, element in enumerate(iterable):
            if i == nexti:
                yield element
                nexti = next(it)
    except StopIteration:
        # Consume to *stop*.
        for i, element in zip(range(i + 1, stop), iterable):
            pass

"""
