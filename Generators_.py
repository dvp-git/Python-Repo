######################
""" GENERATORS """
######################


"""Generators := Generate as and when required. No storing, or returning. YIELD
In order to save memory (and time), use generator functions whenever possible.


#####################

Two types:
1) Generator Expressions:  Similar to list comprehensions. Returns object that produce result one by one.

2) Generator functions : Uses yield instead of return statement. Suspend and resume state

Generator objects also have three other methods that allow us to control their behavior: 
send(), throw(), and close(). 
send() allows us to communicate a value back to the generator object. 
while throw() and close(), respectively, allow us to raise an exception within the generator and close it
"""

# def get_number(n):
#     for i in range(n):
#         yield i


# Ex : 2
# def geometric_progression(a,r):
#     n = 0
#     while True:
#         result = a * r**n
#         if result <= 100000:
#             yield result
#         else:
#             return  # Breaks the iteration protocol : StopIteration raised
#         n += 1

# for n in geometric_progression(2,5):
#     print(n)


""" Send method to generator to stopIteration"""
# def counter(start=0):
#     n = start
#     while True:
#         result = yield n             
#         print(type(result), result)  
#         if result == 'Q':
#             break
#         n += 1
# c = counter()
# print(next(c))         
# print(c.send('Wow!'))  
# print(next(c))         
# print(c.send('Q'))     

"""yield from """
def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))

for n in print_squares(2, 5):
    print(n)
    
""" GENERATOR Expressions : Similar to list but exhausted once called"""

# gen_A  = (x*2 for x in range(2,100))
# >>> list(gen_A)
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]
# >>> list(gen_A)
# []

""" sum() Receives numbers one at a time from generator"""
# s = sum([n**2 for n in range(10**9)])  # this is killed
s = sum(n**2 for n in range(10**9))    # this succeeds
print(s)  # prints: 333333332833333333500000000
