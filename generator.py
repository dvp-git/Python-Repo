# Generator functions

def gener():
    yield 1
    yield 2
    yield 3

g = gener()    # making g a generator. It's a Python iterator now
print(g)

# Use the next keyword to fetch the values of the genrator g

#print(next(g))
#print(next(g))
#print(next(g))

# Can be used in a for loop as a normal iterator

for item in g:
    print(item)
