# List comprehensions
from math import factorial

words = "Why sometimes I have believed as many as six impossible things before breakfast"
words = words.split()
print(words)

print([len(word) for word in words])  # Comprehension example


# General for [ expr(item) for item in iterable]
f = [factorial(x) for x in range(20)]   # the Factorials upto 20
f_length = [len(str(factorial(x))) for x in range(20)]  # Length of the factorials
print(f)
print(f_length)
