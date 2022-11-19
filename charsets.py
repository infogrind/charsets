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

def filter_printable(chars):
    return map(
            lambda c: c if c.isprintable() else '❌',
            chars)

print("\t".join(['Byte'] + list(charsets.keys())))
for x in range(CHAR_FROM, CHAR_TO + 1):
    # First convert the integer to a corresponding (single) byte sequence.
    b = x.to_bytes(1, 'little')
    # For each specified charset, we convert the byte to a (single-character)
    # string by decoding using that specific charset.
    decoded = map(
            lambda i: 'DEL' if x == 127 else b.decode(encoding=charsets[i],errors='replace'),charsets.keys()
            )
    # Print nicely the character from each charset
    print("\t".join(["{}".format(hex(x))] + list(filter_printable(decoded))))
