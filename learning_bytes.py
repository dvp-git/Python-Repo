### New learning about bytes for binary, octal and hexadecimal numbers

### hexadecimal

a = b'\xff\x10'

### Decoding this :

print(a[0])    # Takes ff as the first element[ 1st byte 8 bits ] of the total bytes  = 255
print(a[1])    # Takes 10 as the second element [ 2nd byte 8 bits ] of the total bytes = 16

### Decoding this :

a = b'\10010'

### Decoding this :

print("First",a[0])
print("Second",a[1])
print("Third",a[2])
print(a[3])
print(a[4])
print(a[5])
