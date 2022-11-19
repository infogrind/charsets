#!/usr/bin/env python3

# Program to print single-byte characters using different character encodings.
# This program also illustrates how to use Python's decode() method.

CHAR_FROM = 0
CHAR_TO = 255

charsets = {
        "8859": "iso-8859-1",
        "win": "windows_1252",
        "437": "437",
        "850": "850",
        "utf-8": "utf-8",
        }

# From https://unicode.org/Public/MAPPINGS/VENDORS/MISC/IBMGRAPH.TXT
cp437 = {
        b'\x15': u'\u00A7',
        b'\x14': u'\u00B6',
        b'\x07': u'\u2022',
        b'\x13': u'\u203C',
        b'\x1B': u'\u2190',
        b'\x18': u'\u2191',
        b'\x1A': u'\u2192',
        b'\x19': u'\u2193',
        b'\x1D': u'\u2194',
        b'\x12': u'\u2195',
        b'\x17': u'\u21A8',
        b'\x1C': u'\u221F',
        b'\x7F': u'\u2302',
        b'\xCD': u'\u2550',
        b'\xBA': u'\u2551',
        b'\xC9': u'\u2554',
        b'\xBB': u'\u2557',
        b'\xC8': u'\u255A',
        b'\xBC': u'\u255D',
        b'\xCC': u'\u2560',
        b'\xB9': u'\u2563',
        b'\xCB': u'\u2566',
        b'\xCA': u'\u2569',
        b'\xCE': u'\u256C',
        b'\x16': u'\u25AC',
        b'\x1E': u'\u25B2',
        b'\x10': u'\u25BA',
        b'\x1F': u'\u25BC',
        b'\x11': u'\u25C4',
        b'\x09': u'\u25CB',
        b'\x08': u'\u25D8',
        b'\x0A': u'\u25D9',
        b'\x01': u'\u263A',
        b'\x02': u'\u263B',
        b'\x0F': u'\u263C',
        b'\x0C': u'\u2640',
        b'\x0B': u'\u2642',
        b'\x06': u'\u2660',
        b'\x05': u'\u2663',
        b'\x03': u'\u2665',
        b'\x04': u'\u2666',
        b'\x0D': u'\u266A',
        b'\x0E': u'\u266B',
        }

def filter_printable(chars):
    return map(
            lambda c: c if c.isprintable() else '❌',
            chars)

def decode(b, charset):
    if charset == '437':
        # Special decoding needed because of
        # https://stackoverflow.com/a/46942819
        return decode_cp437(b)
    else:
        return b.decode(encoding=charset,errors='replace')

def decode_cp437(b):
    if b in cp437:
        return cp437[b]
    else:
        return b.decode(encoding='437',errors='replace')


print("\t".join(['Byte'] + list(charsets.keys())))
for x in range(CHAR_FROM, CHAR_TO + 1):
    # First convert the integer to a corresponding (single) byte sequence.
    b = x.to_bytes(1, 'little')
    # For each specified charset, we convert the byte to a (single-character)
    # string by decoding using that specific charset.
    decoded = map(
            lambda i: 'DEL' if x == 127 else decode(b,charsets[i]), charsets.keys()
            )
    # Print nicely the character from each charset
    print("\t".join(["{}".format(hex(x))] + list(filter_printable(decoded))))
