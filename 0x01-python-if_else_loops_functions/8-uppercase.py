#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        # Check if character is between 'a' and 'z'
        if 'a' <= char <= 'z':
            # Convert to uppercase
            print(chr(ord(char) - 32), end="")
        else:
            # Print non-lowercase characters as is
            print(char, end="")
    print()  # New line at the end
