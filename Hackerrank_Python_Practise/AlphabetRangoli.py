# Alphabet Rangoli

#size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# Remember here, we are using the special case of string slicing
# in which, reverse of string is done using the method of slincing [::-1].
# Remember also that the .join() method can be called to concatenate "-"
# between the string codepoints as in x = x = "-".join(alphabets[i:n])

List = []

N = int(input())
# alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
alphabets = "abcdefghijklmnopqrstuvwxyz"


for i in range(N-1,-1,-1):
    if N == 1:
        print(alphabets[N-1])
    else:
        x = "-".join(alphabets[i:N])
        # print(x)
        # print(x[1:])
        List.append((x[::-1]+ x[1:]).center(4*N - 3,"-"))
        # print(List)
# This will join the items of List first, followed by joining List[n-2::-1]. Why ? Because -1 reverses the list,
# and then, adds is (reversed ) up until the 2nd element in the List,
# ( because the first element is already added by List , hence leave it out.)
print('\n'.join(List + List[N-2::-1]))




"""Output for referance:
e

['--------e--------']
d-e
-e
['--------e--------', '------e-d-e------']
c-d-e
-d-e
['--------e--------', '------e-d-e------', '----e-d-c-d-e----']
b-c-d-e
-c-d-e
['--------e--------', '------e-d-e------', '----e-d-c-d-e----', '--e-d-c-b-c-d-e--']
a-b-c-d-e
-b-c-d-e
['--------e--------', '------e-d-e------', '----e-d-c-d-e----', '--e-d-c-b-c-d-e--', 'e-d-c-b-a-b-c-d-e']
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
