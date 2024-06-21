""" Importing neccesary defs from 'lz_defs' """
from lz_defs import LZ77, LZ78, LZW, write_compressed_file, read_compressed_file, read_file, write_decompressed_file

# LZ77
def main_lz77(input_file, output_file):
    """LZ77 main def"""
    lz77 = LZ77(window_size=20)
    data = read_file(input_file)
    compressed = lz77.compress_lz77(data)
    write_compressed_file(output_file, compressed)
    print(f'Compressed data written to {output_file}')
    

def decompress_file_lz77(input_file, output_file):
    """LZ77 decompressing def"""
    lz77 = LZ77(window_size=20)
    compressed = read_compressed_file(input_file)
    decompressed = lz77.decompress_lz77(compressed)
    with open(output_file, 'w') as file:
        file.write(decompressed)
    print(f'Decompressed data written to {output_file}')
#-------------------------------------------------------


#LZ78
def main_lz78(input_file, output_file):
    """LZ78 main def"""
    lz78 = LZ78()
    data = read_file(input_file)
    compressed = lz78.compress_lz78(data)
    write_compressed_file(output_file, compressed)
    print(f'Compressed data written to {output_file}')


def decompress_file_lz78(input_file, output_file):
    """LZ78 decompressing def"""
    lz78 = LZ78()
    compressed = read_compressed_file(input_file)
    decompressed = lz78.decompress_lz78(compressed)
    write_decompressed_file(output_file, decompressed)
    print(f'Decompressed data written to {output_file}')
#-------------------------------------------------------


#LZW
def main_lzw(input_file, output_file):
    """LZW main def"""
    lzw = LZW()
    data = read_file(input_file)
    compressed = lzw.compress_lzw(data)
    write_compressed_file(output_file, compressed)
    print(f'Compressed data written to {output_file}')


def decompress_file_lzw(input_file, output_file):
    """LZW decompressing def"""
    lzw = LZW()
    compressed = read_compressed_file(input_file)
    decompressed = lzw.decompress_lzw(compressed)
    write_decompressed_file(output_file, decompressed)
    print(f'Decompressed data written to {output_file}')
#-------------------------------------------------------

# Initialization
if __name__ == '__main__':

    meth = input('Choose LZ-method (1 for LZ77, 2 - for LZ78, 3 - for LZW) >> ')
    input_file = 'py/1_course/tic_labs/input.txt'

    if meth == '1':  # LZ77
        main_lz77(input_file, 'py/1_course/tic_labs/output.lz77')
        decompress_file_lz77('py/1_course/tic_labs/output.lz77', 'py/1_course/tic_labs/decompressed_lz77.txt')

    elif meth == '2':  # LZ78
        main_lz78(input_file, 'py/1_course/tic_labs/output.lz78')
        decompress_file_lz78('py/1_course/tic_labs/output.lz78', 'py/1_course/tic_labs/decompressed_lz78.txt')
    
    elif meth == '3':  # LZW
        main_lzw(input_file, 'py/1_course/tic_labs/output.lzw')
        decompress_file_lzw('py/1_course/tic_labs/output.lzw', 'py/1_course/tic_labs/decompressed_lzw.txt')
    
    else:  # Warning about incorrect choice
        print('Incorrect choice! Please retry!')
        exit()
