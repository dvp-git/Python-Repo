import sys

def convert(s):
    """ Convert to an integer"""
    if not isinstance(s,str):
        raise TypeError("Argument must be a string ")
    try  :
        return int(s)
    except (ValueError,TypeError) as e:
        print("Conversion Error : {}".format(str(e),file = sys.stderr))
    else:
        print(s)

convert(89)
