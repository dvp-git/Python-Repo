# Writing binary file_sizes

""" A module for dealing with BMP bitmap image files"""

def write_grayscale(filename,pixels): # Grayscale images ( 8 - bit ) have a proerty that they are 1 byte per pixe
        """Creates and writes a grayscale BMP file.

        Args:
            filename: The name of the BMP file to be created
            pixels: A rectangular image stored as a sequence of rows. Each row must be an iternble series of integers in range 0-255

            Pixel : Each int is a pixel value from 0 - 255.
            Outer row : List of pixel rows from top to bottom.
            Inner row : Row of pixels from left to right.
        Raises :
            OSError: If the file couldn't be written"""

        height = len(pixels)
        width = len(pixels[0])

# b'\x00' --> The b is binary file , \x means hexadecimal numbers ,
        with open(filename,'wb') as bmp:
            # Header
            #BMP type
            bmp.write(b'BM')                    # Magic byte sequence. BM to indicate BMP image

            # Size of the file
            size_bookmark = bmp.tell()          # The next 4 bytes hold the filesize as 32-bit. Tell() method stores byte offset from beginning of the file to current line
            bmp.write(b'\x00\x00\x00\x00')      # litte endian. Least significant Byte is written first.  For now write 0 bytes.


            bmp.write(b'\x00\x00')              # Placeholder for holding unsigned 16-bit integer
            bmp.write(b'\x00\x00')              # Placeholder for holding unsigned 16-bit integer

            pixel_offset_bookmark = bmp.tell()         # Pixel offset to hold the pixel start offset
            bmp.write(b'\x00\x00\x00\x00')      # Pixe data. Zero placeholder for now

            # Info Image header
            bmp.write(b'\x28\x00\x00\x00')      # Image header size.Decimal value 40 - Least significant byte is written first /

            # Dimensions
            bmp.write(_int32_to_bytes(width))   # Image width in pixels (Contains exactly 4 bytes)
            bmp.write(_int32_to_bytes(height))  # Image height in pixels
            bmp.write(b'\x01\x00')              # Number of image planes
            bmp.write(b'\x08\x00')              # Bits per pixel 8 for grayscale. no of colors = 256

            # Compression type
            bmp.write(b'\x00\x00\x00\x00')      # No compression
            bmp.write(b'\x00\x00\x00\x00')      # Zero for uncompressed images
            bmp.write(b'\x00\x00\x00\x00')      # Unused pixels per meter [ Horizontal resolution]
            bmp.write(b'\x00\x00\x00\x00')      # Unused pixels per meter [ Vertical resoluton ]

            # Color format
            bmp.write(b'\x00\x00\x00\x00')      # Use whole color table
            bmp.write(b'\x00\x00\x00\x00')      # All colors are important

            # Color Paletter - Linear grayscale
            for c in range(256):
                bmp.write(bytes((c,c,c,0)))     # Blue , Green , Red , Zero

            # Pixel data
            pixel_data_bookmark = bmp.tell()

            for row in reversed(pixels):        # The BMP image is written bottom to top, so reverse the rows
                row_data = bytes(row)
                bmp.write(row_data)
                padding = b'\x00' * ( 4 - len(row) % 4)  # because each row_data should be a mutilple of 4 bytes
                bmp.write(padding)

            # End of file bookmark
            eof_bookmark = bmp.tell()

            # Filling in the size placeholder
            bmp.seek(size_bookmark)             # Get back to the size bookmark point in the file
            bmp.write(_int32_to_bytes(eof_bookmark))    # Fill in the bytes upto end of bookmark pointer

            # Filling in the pixel offset placeholder
            bmp.seek(pixel_offset_bookmark)
            bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    """Convert an integer which is 32 bits into 4 bytes using right shift operator"""
    return bytes((i & 0xff, i >> 8 & 0xff , i >> 16 & 0xff , i >> 24 & 0xff))


write_grayscale('gray.bmp',[[255,135,150],[0,0,0],[60,110,75],[0,200,150],[255,245,150],[155,135,67],
                            [255,135,150],[0,0,0],[60,110,75],[0,200,150],[255,245,150],[155,135,67],
                            [255,135,150],[0,0,0],[60,110,75],[0,200,150],[255,245,150],[155,135,67],
                            [255,135,150],[0,0,0],[60,110,75],[0,200,150],[255,245,150],[155,135,67],
                            [255,135,150],[0,0,0],[60,110,75],[0,200,150],[255,245,150],[155,135,67],
                            [255,135,150],[0,0,0],[60,110,75],[0,200,150],[255,245,150],[155,135,67],
                            [255,135,150],[0,0,0],[60,110,75],[0,200,150],[255,245,150],[155,135,67],
                            ])    ## Produces a black pixel image since values are [0 0 0] [0 0 0]
