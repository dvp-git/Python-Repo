#######################################
""" Files and Data Persistence """
#######################################
"""
Files and directories : os , pathlib, shutil

Compression

Networks and streams

The JSON data-interchange format

Data persistence with pickle and shelve, from the standard library

Data persistence with SQLAlchemy
"""

# with open('print_example.txt','w') as filObj:
#     print("Hey I'm writing to this file",file=filObj)

# with open('fear.txt') as f:
#     lines = [line.rstrip() for line in f]

# # print(lines)
# with open('fear_copy.txt', 'w') as fw:
#     fw.write('\n'.join(lines))

# Opening a file in binary mode:
with open('example.bin','wb') as fbw:
    fbw.write(b'This is binary data ...')
with open('example.bin','rb') as fbr:
    print(fbr.read())

# Use 'x' to check if file is present. If not present it writes, else it fails.
with open('write_x.txt', 'x') as fw:  # this succeeds
    fw.write('Writing line 1')

with open('write_x.txt', 'x') as fw:  # this fails FileExistsError: [Errno 17] File exists: 'write_x.txt
    fw.write('Writing line 2')


from pathlib import Path

p = Path('fear.txt')

path_parent = p.parent.absolute()
print("Path parent {}".format(path_parent))
path_parent.is_dir()

path_file  = p.absolute()
print("Path file {}".format(path_file))
path_file.is_file()
