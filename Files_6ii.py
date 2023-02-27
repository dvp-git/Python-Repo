# Files_6.py try finally block execution

''' Reading the Recamman series data file back in '''
import sys

def read_sequence(filename):
    try:
        ### Using the try finally block so that the file always closes once opened to avoid any memory leaks
        f = open(filename, mode = 'rt', encoding = 'utf-8')
        series = []
        for line in f:
            a = int(line.strip())
            series.append(a)
            # return [int(line.strip()) for line in f ]
    finally:
        f.close()
    return series

def main(filename):
    series = read_sequence(filename)
    print(series)

if __name__ == "__main__":
    main(sys.argv[1])       # Pass the file Files_6.dat
