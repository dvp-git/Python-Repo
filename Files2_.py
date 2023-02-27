##################################
# File manaipulation 
##################################
# from collections import Counter
# from string import ascii_letters

# chars = ascii_letters + ' '


# def sanitize(string_ , chars):
#     return ''.join(c for c in string_ if c in chars)

# def reverse(string_):
#     return string_[::-1]

# with open('fear.txt') as stream:
#     lines = [line.rstrip() for line in stream]

# print("Reading lines{}".format(lines)) # List of lines as strings
# print()
# with open('raef.txt','w') as stream:
#     stream.write('\n'.join(reverse(line) for line in lines))

# lines = [sanitize(string_,chars) for string_ in lines]
# print("After Sanitizing .. {}".format(lines))

# print()


# whole = ' '.join(lines)
# print("Joining lines .. {}".format(whole))

# print()


# cnt = Counter(whole.lower().split())

# print("cnt={}".format(cnt))
# print("Most common words.. {}".format(cnt.most_common(5)))


"""
Manipulation more oriented to disk operations

pathlib library: / operator to concatenate directory names; 
pathlib takes care of using the right path separator for us, behind the scenes.



"""
# import shutil
# from pathlib import Path


# base_path = Path('ops_example')
# print(f"{type(base_path)},{base_path}")

# # Remove if there exists a tree directory structure.
# if base_path.exists() and base_path.is_dir():
#     shutil.rmtree(base_path)

# base_path.mkdir()

# path_b = base_path / 'A' / 'B'
# path_c = base_path / 'A' / 'C'
# path_d = base_path / 'A' / 'D'

# path_b.mkdir(parents=True)
# path_c.mkdir()

# # Add files in these directories:
# for file_ in ('ex1.txt','ex2.txt','ex3.txt'):
#     with open(path_b / file_,'w') as stream:
#         stream.write('Some context in {}\n'.format(file_))

# shutil.move(path_b, path_d) # Move file to different location. B is deleted

# ex1 = path_d / 'ex1.txt'


# ex1.rename(ex1.parent /  'ex1.renamed.txt')
# # print("Path B {}".format(path_b))

"""
###########
# Temporary files and directories
###########

"""
# from tempfile import TemporaryDirectory, NamedTemporaryFile



# # Creates a temp diretory, and file and deletes after execution.
# with TemporaryDirectory(dir=".") as td:
#     print("Temp directory :", td)
#     with NamedTemporaryFile(dir=td) as t:
#         name = t.name
#         print(name)


# Inspecting content:
from pathlib import Path

p = Path('.')    # Current directory
# p.glob(pattern)
# Help on method glob in module pathlib:

# glob(pattern) method of pathlib.WindowsPath instance
#     Iterate over this subtree and yield all existing files (of any
#     kind, including directories) matching the given relative pattern.

# for file_ in p.glob('*'):
#     print("File: " if file_.is_file() else "Folder:",file_)
#     print(len(file_))

# Folder: .git
# Folder: .vscode
# File:  Decorators.py
# File:  example.bin
# File:  Exceptions_.py
# File:  fear.txt
# File:  fear_copy.txt
# File:  Files2_.py
# File:  Files_.py
# File:  Functions.py
# File:  Generators_.py
# File:  MapFilterZip.py
# File:  OOPs.py
# Folder: ops_example
# File:  print_example.txt
# File:  raef.txt
# File:  static_class_methods.py


""" Alternate way to print files,"""

# import os
# for root, dirs, files in os.walk('.'):
#     abs_root = os.path.abspath(root)
#     print(abs_root)
#     if dirs:
#         print('Directories:')
#         for dir_ in dirs:
#             print(dir_)
#         print()
#     if files:
#         print('Files:')
#         for filename in files:
#             print(filename)
#         print()

#########################3
# Compressing files:
###########################
from zipfile import ZipFile
with ZipFile('example.zip','w') as zp:
    zp.write('fear.txt')
    zp.write('raef.txt')
    zp.write('ops_example/A/D/ex2.txt')

with ZipFile('example.zip') as zp:

    # extract(source_file, target_folder)
    zp.extract('fear.txt','extract_zip')
    zp.extract('ops_example/A/D/ex2.txt','extract_zip/C')
