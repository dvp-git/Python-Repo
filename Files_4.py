# Files as iterators

import sys

def main(filename):
    with open(filename, mode = 'rt', encoding = 'utf-8') as fileObj:
        for line in fileObj:
                # Use the strip method to remove the newline character printed by thr for loop
                print(line.strip())


if "__main__" == __name__:
    main(sys.argv[1])
 
