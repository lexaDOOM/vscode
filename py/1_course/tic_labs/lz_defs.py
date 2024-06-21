import pickle

class LZ77:
    """LZ77 class with its methods"""
    def __init__(self, window_size=20):
        self.window_size = window_size
    
    def compress_lz77(self, data):  # LZ77 compression method
        i = 0
        output = []
        while i < len(data):
            match = self.longest_match_lz77(data, i)
            if match:
                (best_match_distance, best_match_length) = match
                output.append((best_match_distance, best_match_length, data[i + best_match_length]))
                i += best_match_length + 1
            else:
                output.append((0, 0, data[i]))
                i += 1
        return output

    def decompress_lz77(self, compressed):  # LZ77 decompression method
        decompressed = []
        for item in compressed:
            (distance, length, char) = item
            if distance == 0 and length == 0:
                decompressed.append(char)
            else:
                start = len(decompressed) - distance
                for _ in range(length):
                    decompressed.append(decompressed[start])
                    start += 1
                decompressed.append(char)
        return ''.join(decompressed)

    def longest_match_lz77(self, data, current_position):
        end_of_buffer = min(current_position + self.window_size, len(data) + 1)
        best_match_distance = -1
        best_match_length = -1
        for j in range(current_position + 2, end_of_buffer):
            start_index = max(0, current_position - self.window_size)
            substring = data[current_position:j]
            for i in range(start_index, current_position):
                repeat_length = j - current_position
                if data[i:i + repeat_length] == substring:
                    if repeat_length > best_match_length:
                        best_match_distance = current_position - i
                        best_match_length = repeat_length
        if best_match_distance > 0 and best_match_length > 0:
            return (best_match_distance, best_match_length)
        return None


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_compressed_file(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def read_compressed_file(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def decompress_file(input_file, output_file):
    lz77 = LZ77(window_size=20)
    compressed = read_compressed_file(input_file)
    decompressed = lz77.decompress_lz77(compressed)
    with open(output_file, 'w') as file:
        file.write(decompressed)
    print(f'Decompressed data written to {output_file}')



class LZ78:
    """LZ78 class with its methods"""
    def compress_lz78(self, data):
        dictionary = {}
        dictionary_size = 1
        current_string = ""
        output = []
        for char in data:
            current_string_plus_char = current_string + char
            if current_string_plus_char in dictionary:
                current_string = current_string_plus_char
            else:
                if current_string == "":
                    output.append((0, char))
                else:
                    output.append((dictionary[current_string], char))
                dictionary[current_string_plus_char] = dictionary_size
                dictionary_size += 1
                current_string = ""
        if current_string:
            output.append((dictionary[current_string], ""))
        return output

    def decompress_lz78(self, compressed):
        dictionary = {0: ""}
        dictionary_size = 1
        decompressed = []
        for index, char in compressed:
            if index in dictionary:
                entry = dictionary[index] + char
            else:
                entry = char
            decompressed.append(entry)
            dictionary[dictionary_size] = entry
            dictionary_size += 1
        return ''.join(decompressed)

def write_decompressed_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)


class LZW:
    """LZW class with its methods"""
    def compress_lzw(self, uncompressed):
        # Build the dictionary.
        dict_size = 256
        dictionary = {chr(i): i for i in range(dict_size)}
        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                # Add wc to the dictionary.
                dictionary[wc] = dict_size
                dict_size += 1
                w = c

        # Output the code for w.
        if w:
            result.append(dictionary[w])
        return result

    def decompress_lzw(self, compressed):
        # Build the dictionary.
        dict_size = 256
        dictionary = {i: chr(i) for i in range(dict_size)}

        # use iter to create an iterator and next to get the first value
        result = []
        w = chr(compressed[0])
        result.append(w)
        for k in compressed[1:]:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0]
            else:
                raise ValueError('Bad compressed k: %s' % k)
            result.append(entry)

            # Add w+entry[0] to the dictionary.
            dictionary[dict_size] = w + entry[0]
            dict_size += 1

            w = entry
        return ''.join(result)

