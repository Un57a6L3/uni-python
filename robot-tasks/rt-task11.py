from struct import unpack


def main(file):
    # Find starting address
    a_adr = 0
    for byte in file:
        a_adr += 1
        if byte == 0xba:
            break

    # Unpack data for structure A (32 bytes)
    a = {f'A{i}': None for i in range(1, 8)}
    temp = unpack('<LfLLHhQHH', file[a_adr:a_adr + 32])
    b_adr, a['A2'], ch_size, ch_adr, d_adr, \
        a['A5'], a['A6'], f_size, f_adr = temp

    # A3 (char array)
    temp = unpack(f'<{ch_size}s', file[ch_adr:ch_adr + ch_size])
    a['A3'] = str(temp[0], 'utf8')

    # A7 (float array)
    temp = unpack(f'<{f_size}f', file[f_adr:f_adr + f_size * 4])
    a['A7'] = list(temp)

    # Unpack data for structure B (18 bytes)
    b = {f'B{i}': None for i in range(1, 4)}
    temp = unpack('<LLLHL', file[b_adr:b_adr + 18])
    ch_size, ch_adr, b['B2'], c_size, c_adr = temp

    # B1 (char array)
    temp = unpack(f'<{ch_size}s', file[ch_adr:ch_adr + ch_size])
    b['B1'] = str(temp[0], 'utf8')

    # Unpack data for structures C (14 bytes)
    c_adrs = unpack(f'<{c_size}I', file[c_adr:c_adr + c_size * 4])
    b['B3'] = []
    for adr in c_adrs:
        temp = unpack(f'<hqI', file[adr:adr + 14])
        c1, c2, c3 = temp
        b['B3'].append({'C1': c1, 'C2': c2, 'C3': c3})

    # Unpack data for structure D (33 bytes)
    d = {f'D{i}': None for i in range(1, 4)}
    temp = unpack(f'<bf7i', file[d_adr:d_adr + 33])
    d['D1'], d['D2'] = temp[:2]
    d['D3'] = list(temp[2:])

    # Assign structures B and D to A1 and A4
    a['A1'] = b
    a['A4'] = d
    return a


# --- cut this out when submitting to robot ---
data1 = (
    b'DTCN\xba\x82\x00\x00\x00\x03\x07\xdd>\x02\x00\x00\x00\x94\x00\x00'
    b'\x00\x96\x00\x16\xdd\x18\xc2\x91\x12 `\x02\x1a\x02\x00\xb7\x00iocdx\x8f\xa7'
    b'\xa9\xc6qX\x88ykD\xd5\x8a\x10\r\x8b\x90\xbc-?\xce|U3\x00\x8d\x17'
    b'\xbc\x01\xd5\xe4)bf\x13\rc\xcb\x9fy:\x1e\xd3\xdf\xae\x89\xe6\x00\xcf\xc8\xf0'
    b'y\xfab\xe2\xfeP\xc7N\x85\x7f.\x0e"\x06\x98\xbb\xfe\x08(\x00\x00\x006\x00'
    b'\x00\x00D\x00\x00\x00R\x00\x00\x00`\x00\x00\x00\x03\x00\x00\x00%\x00'
    b'\x00\x00U*o\x8b\x05\x00n\x00\x00\x00fa\x053\x08k>\xb4\x1faw\xff<\xc4\xb6Q'
    b'm\xea\xed\xa2\x15x \xf9P\xe5\xcb\xf5_\x81\xd4\x8eB6\x8c\x89\x86\x14>\xcf'
    b'\x15h?'
)

data2 = (
    b'DTCN\xbao\x00\x00\x00,\x96\xba>\x02\x00\x00\x00\x81\x00\x00\x00\x83\x00\xbc'
    b'>\x8aM\x1bJT\xd3_\xf2\x02\x00\xa4\x00rk#J\xe4\x8b\r\xd5=\x0c\xe5t\xb0A\xf5'
    b'x\xe6f\xa8C8\xa8qCB\x10\x9d8\xb5\xb6y\xa7\x9f\xe8\x1f\xd8\xaa\xd1\xa9'
    b"\xa7\xfb\xee>\xb4~\x0fgI\xc9L\x9d\xdc\xd5\xdani\xf2\xab'\x00\x00\x005"
    b'\x00\x00\x00C\x00\x00\x00Q\x00\x00\x00\x02\x00\x00\x00%\x00\x00\x00c'
    b'\r\x08"\x04\x00_\x00\x00\x00ti\xf8\x0b\xb06\xbf=_\xa9\x11{d\x0b\x08'
    b"\xcbV.\x93\xd8\x14\xb7\xe9\x07\xcd\xc5M\x82B\xf0\xeb?\xdb0'\x10\x7fD\xbf"
    b'\xcd\x82N\xbf'
)

print(main(data1))
print(main(data2))
