# Single-byte Characters Printed using Different Charsets

This program demonstrates how to use different encodings in Python to convert
raw bytes to string characters.

Note that single-byte values larger than 127 can't be decoded using `utf-8`,
because `utf-8` uses more than one byte for non-ASCII characters.

