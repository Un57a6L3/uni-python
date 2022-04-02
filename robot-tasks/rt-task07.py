def main(num):
    # isolate input sections
    a = num & 0x00000003  # (2 ** 2  - 2 ** 0)
    b = num & 0x0003fffc  # (2 ** 18 - 2 ** 2)
    c = num & 0x0ffc0000  # (2 ** 28 - 2 ** 18)
    d = num & 0x30000000  # (2 ** 30 - 2 ** 28)
    e = num & 0xc0000000  # (2 ** 32 - 2 ** 30)

    # transform sections to output
    return (a << 30) | (b >> 2) | c | (d >> 12) | (e >> 2)


# --- cut this out when submitting to robot ---

# takes border positions, prints masks for each section
def convert():
    s = [0, 2, 18, 28, 30, 32]   # numbers to the left of each border
    for i in range(len(s) - 1):  # f-string expressions are cool
        print(f"{chr(ord('A') + i)}: 0x{(2 ** s[i + 1] - 2 ** s[i]):08x}")


print(f'0x{main(0xb163e58f):08x}')
print(f'0x{main(0x29daf9f4):08x}')
