def decompress_rle(encoded_string):
    new_string = ''
    counter = ''
    skipper = -1
    for i in range(len(encoded_string)):
        '10X1Y12B5C'
        if i == skipper:
            continue
        if encoded_string[i] in '0123456789':
            if encoded_string[i+1] in '0123456789':
                counter = encoded_string[i] + encoded_string[i+1]
                counter = int(counter)
                skipper = i + 1
                new_string += counter * encoded_string[i+2]

            else:
                counter = encoded_string[i]
                counter = int(counter)
                new_string += counter * encoded_string[i+1]

    return new_string

print(decompress_rle("3A2B4C"))   
print(decompress_rle("1W4B1W")) 
print(decompress_rle("10X1Y"))
print(decompress_rle("1A1B1C1D1E"))
print(decompress_rle("12Z"))