### Demonstrating the try finally block for files..
import sys
from itertools import count,islice

"""
Recaman's Sequence
 a_n = {a_(n-1)-n   if a_(n-1)-n > 0 and is new;
       a_(n-1)+n   otheriwse,
(1)
which can be succinctly defined as "subtract if you can otherwise add
The first few terms are 1, 3, 6, 2, 7, 13, 20, 12, 21, 11
"""

# Generating the Recamman's sequence
def sequence():
    """ Generate the Recaman's sequence"""
    seen = set()
    print(seen)
    a = 0
    for n in count(1):                                               # Count will generate an iterable starting from 1
        # if a > 100 :
        #     break
        yield a                                                      # Yield returns the value from the for loop back to the sequence()
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c

# Writing the output to a file to demonstrate the try finally block
def write_sequence(filename, num):
    """Write the Recamman's sequence to a data file"""
    f = open(filename, mode = 'wt', encoding = 'utf-8')
    f.writelines("{0}\n".format(r) for r in islice(sequence(), num + 1))    # The islice function truncates the sequence , islice(iterable,stop_value)
    f.close()

if __name__ == "__main__":
    write_sequence(filename = sys.argv[1], num = int(sys.argv[2]))
