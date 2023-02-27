# Reading binary files:

# Get the dimesons of the BMP image in pixels

def dimensions(filename):
    """ Determine the dimensions of a BMP image in pixel_offset_bookmark

    Args:
        filename : THe name of the BMP image file.

    Returns:
        A tuple containing 2 integers with the width and height in pixels.

    Raise:
        ValueError: If the file was not a BMP files
        OSError: If there was a problem reading the files
    """

    with open(filename,'rb') as f:     # Read binary
        magic = f.read(2)              # First to magic bytes should be b'BM'
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        f.seek(18)          # From the start of the BMP file upto pixel data dimensions , there are exactly 18 bytes
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes), _bytes_to_int32(height_bytes))


def _bytes_to_int32(b):
    """ Converts 4 bytes to integer value ( 32 bit integer)"""
    return b[0] | b[1] << 8 | b[2] << 16 | b[3] << 24


def _int32_to_bytes(i):
    """ Converts a 32 bit integer to 4 bytes"""
    return bytes(( i & 0xff , i >> 8 & 0xff , i >> 16 & 0xff , i >> 24 & 0xff))


dim = dimensions('gray.bmp')
print(dim)
