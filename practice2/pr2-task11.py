from itertools import groupby


# --- Run-Length Encoding (RLE) ---

# Run-Length Encoding algorithm
def rle_encode(input_str):
    input_str = input_str.replace(chr(9794), '')
    mid_result = [(k, len(list(g))) for k, g in groupby(input_str)]
    output = str()
    for i in mid_result:
        for j in i:
            output += str(j)
    return output


# --- Burrows-Wheeler Transform (BWT) ---

# --- IMPORTANT ---
# TLDR: Transform is not efficient

# The end-of-line (EOL) symbol is supposed to be skipped in sorting, but put in the end if it matters somehow
# I have not managed to achieve this task without writing a sorting algorithm, and so have others it seems
# I decided not to bother and leave it as is, resulting in less efficient RLE encoding on output data
# --- --------- ---

# This version was written by me with my codestyle
# and a lot of C++ and C# experience, so it looks like this
def transform_bwt(input_str):
    table = list()
    input_str += chr(9794)
    temp_str = input_str
    rotate = True

    # adding all string rotations to list
    while rotate:
        table.append(temp_str)
        temp_str = temp_str[-1] + temp_str[0:-1]
        # print(temp_str)
        if temp_str == input_str:
            rotate = False

    # sorting and getting results
    table.sort()
    output_str = str()
    for i in range(len(table)):
        output_str += table[i][-1]
    return output_str


# This version was written by someone on the internet
# This takes advantage of Python features and is much more compact
def bwt(s):
    s = s + chr(9794)
    n = len(s)
    m = sorted(s[i:] + s[:i] for i in range(n))
    return ''.join(x[-1] for x in m)


# --- Inverse Burrows-Wheeler Transform ---

# This version was written by me with my codestyle
# and a lot of C++ and C# experience, so it looks like this
def inverse_bwt(input_str):
    n = len(input_str)
    table = [''] * n

    # adding columns and sorting rows
    for _ in range(n):
        for j in range(n):
            table[j] = input_str[j] + table[j]
        table.sort()

    # getting result string
    for j in range(n):
        if table[j][-1] == chr(9794):
            return table[j][:-1]


# This version was written by someone on the internet
# This takes advantage of Python features and is much more compact
def ibwt(s):
    n = len(s)
    m = [''] * n
    for _ in range(n):
        m = sorted(s[i] + m[i] for i in range(n))
    return [x for x in m if x.endswith(chr(9794))][0][:-1]


# --- Main section ---

def main():
    input_str = input('Enter string: ')
    tfd_str1 = transform_bwt(input_str)
    tfd_str2 = bwt(input_str)

    print('BWT transform results:')
    print(f'My algorithm:      \'{tfd_str1}\'')
    print(f'Compact algorithm: \'{tfd_str2}\'')
    print()

    inv_str1 = inverse_bwt(tfd_str1)
    inv_str2 = ibwt(tfd_str2)

    print('Inverse BWT transform results:')
    print(f'My algorithm:      \'{inv_str1}\'')
    print(f'Compact algorithm: \'{inv_str2}\'')
    print()

    enc_str1 = rle_encode(tfd_str1)
    print('RLE encoding results:')
    print(enc_str1)


if __name__ == '__main__':
    main()
