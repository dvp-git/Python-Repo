
filename_1 = 'text_analysis_test_file.txt'
with open(filename_1,'w') as fp:
    fp.write("Now we are engaged in a civil war\n"
             "testing whether the nation\n"
             "or any nation so conceived and so dedicated,\n"
             "can long endure")

def analyze_text(filename):
    """ Calculate the number of lines and characters in the files

    Args :
          filename: The name of the file to analyze

    Raises:
            IOError: If the "filename" does not exist or can't be read

    Returns: A tuple where the first element is the nummber of lines in the file and second element is the number of chracters
    """
    lines = 0
    chars = 0
    with open(filename,'r') as fp:
        for line in fp:
            print("Line ",line)
            lines += 1
            print("CHars: ",chars)
            chars += len(line)
        return (lines, chars)

a_tup = analyze_text(filename_1)
print(a_tup)
