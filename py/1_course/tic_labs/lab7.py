""" Importing neccesary defs from 'lz_defs' """
from lz_defs import LZ77, LZ78, LZW, write_compressed_file, read_compressed_file, read_file, write_decompressed_file
import timeit

# LZ77
def main_lz77(input_file, output_file):
    """LZ77 main def"""
    lz77 = LZ77(window_size=20)
    data = read_file(input_file)
    input_length_lz77 = len(data)  # Input data length measurement

    lz77_compress_s_time = timeit.default_timer()  # LZ77 compress start time
    compressed = lz77.compress_lz77(data)
    lz77_compress_total_time = timeit.default_timer() - lz77_compress_s_time  # LZ77 compress total time
    compressed_length_lz77 = len(compressed)  # Compressed data length measurement

    write_compressed_file(output_file, compressed)
    print(f'\nCompressed data written to {output_file}\nTime elapsed: {lz77_compress_total_time}\n\
Input data length: {input_length_lz77}\nCompressed data length: {compressed_length_lz77}')
    

def decompress_file_lz77(input_file, output_file):
    """LZ77 decompressing def"""
    lz77 = LZ77(window_size=20)
    compressed = read_compressed_file(input_file)

    lz77_decompress_s_time = timeit.default_timer()  # LZ77 decompress start time
    decompressed = lz77.decompress_lz77(compressed)
    lz77_decompress_total_time = timeit.default_timer() - lz77_decompress_s_time  # LZ77 decompress total time

    with open(output_file, 'w') as file:
        file.write(decompressed)
    print(f'\nDecompressed data written to {output_file}\nTime elapsed: {lz77_decompress_total_time}')
#-------------------------------------------------------


#LZ78
def main_lz78(input_file, output_file):
    """LZ78 main def"""
    lz78 = LZ78()
    data = read_file(input_file)
    input_length_lz78 = len(data)  # Input data length measurement

    lz78_compress_s_time = timeit.default_timer()  # LZ78 compress start time
    compressed = lz78.compress_lz78(data)
    lz78_compress_total_time = timeit.default_timer() - lz78_compress_s_time  # LZ78 compress total time
    compressed_length_lz78 = len(compressed)  # Compressed data length measurement

    write_compressed_file(output_file, compressed)
    print(f'\nCompressed data written to {output_file}\nTime elapsed: {lz78_compress_total_time}\n\
Input data length: {input_length_lz78}\nCompressed data length: {compressed_length_lz78}')


def decompress_file_lz78(input_file, output_file):
    """LZ78 decompressing def"""
    lz78 = LZ78()
    compressed = read_compressed_file(input_file)

    lz78_decompress_s_time = timeit.default_timer()  # LZ78 decompress total time
    decompressed = lz78.decompress_lz78(compressed)
    lz78_decompress_total_time = timeit.default_timer() - lz78_decompress_s_time  # LZ78 decompress total time

    write_decompressed_file(output_file, decompressed)
    print(f'\nDecompressed data written to {output_file}\nTime elapsed: {lz78_decompress_total_time}')
#-------------------------------------------------------


#LZW
def main_lzw(input_file, output_file):
    """LZW main def"""
    lzw = LZW()
    data = read_file(input_file)
    input_length_lzw = len(data)  # Input data length measurement

    lzw_compress_s_time = timeit.default_timer()  # LZW compress start time
    compressed = lzw.compress_lzw(data)
    lzw_compress_total_time = timeit.default_timer() - lzw_compress_s_time  # LZW compress total time
    compressed_length_lzw = len(compressed)  # Compressed data length measurement

    write_compressed_file(output_file, compressed)
    print(f'\nCompressed data written to {output_file}\nTime elapsed: {lzw_compress_total_time}\n\
Input data length: {input_length_lzw}\nCompressed data length: {compressed_length_lzw}')


def decompress_file_lzw(input_file, output_file):
    """LZW decompressing def"""
    lzw = LZW()
    compressed = read_compressed_file(input_file)

    lzw_decompress_s_time = timeit.default_timer()  # LZW decompress start time
    decompressed = lzw.decompress_lzw(compressed)
    lzw_decompress_total_time = timeit.default_timer() - lzw_decompress_s_time  # LZW decompress total time

    write_decompressed_file(output_file, decompressed)
    print(f'\nDecompressed data written to {output_file}\nTime elapsed: {lzw_decompress_total_time}')
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
    
    elif meth == 'blue':  # Easter egg
        print("- Say my name!\n- Heisenberg!\n- You're goddamn right!")
        exit()
        
    
    else:  # Warning about incorrect choice
        print('Incorrect choice! Please retry!')
        exit()
