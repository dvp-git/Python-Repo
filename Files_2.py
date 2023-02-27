#Reading a file:

g = open('wasteland.txt', mode = 'rt' , encoding = 'utf-8')
f = g.readlines()
print(f)
g.close()

"""
g.seek(0) is used to move the read line pointer to the start of the file

g. readlines() - returns a list containing all the contents of the files
"""
