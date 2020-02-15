## Filtering predicates

# Prime number test
from math import sqrt

def is_prime(x):
    if x < 2 :
        return False
    for i in range(2,int(x)):
        if x % i == 0:
             return False
    return True



#print([x for x in range(101) if is_prime(x)])

#print({x*x:(1,x,x*x) for x in range(100) if is_prime(x)})
