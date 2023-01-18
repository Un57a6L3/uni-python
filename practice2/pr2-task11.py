from itertools import groupby
EOL = chr(9830)

# --- IMPORTANT: BWT Transform is not fully efficient ---
# The end-of-line (EOL) symbol is supposed to be skipped in sorting, but not omitted
# Doing that would require writing a special sorting algorithm instead of using sort()
# I decided to leave it as is, resulting in slightly less efficient RLE encoding on output data


# Run-Length Encoding (RLE)
def rle_encode(data):
    data = data.replace(EOL, '')                             # removing EOL symbol from string
    output = [(k, len(list(g))) for k, g in groupby(data)]   # encoding: outputs list[tuple(str, int)]
    return ''.join(f'{ch}{num}' for ch, num in output)       # parsing the output into a string


# Burrows-Wheeler Transform (BWT)
def transform_bwt(data):
    data += EOL                                              # appending EOL symbol to string
    table = [data[i:] + data[:i] for i in range(len(data))]  # adding all string rotations to list
    return ''.join(t[-1] for t in sorted(table))             # sorting list and getting results


# Inverse Burrows-Wheeler Transform
def inverse_bwt(data):
    n = len(data)                                           # creating empty string list
    table = [''] * n                                        #
    for _ in range(n):                                        # adding columns and sorting rows
        table = sorted(data[j] + table[j] for j in range(n))  #
    return [x[:-1] for x in table if x[-1] == EOL][0]       # getting result string


def main():
    input_str = input('Enter string: ')
    tfd_str = transform_bwt(input_str)
    print(f'BWT transform results:         \'{tfd_str}\'')
    inv_str = inverse_bwt(tfd_str)
    print(f'Inverse BWT transform results: \'{inv_str}\'')
    enc_str = rle_encode(tfd_str)
    print(f'RLE encoding results:          \'{enc_str}\'')


if __name__ == '__main__':
    main()
