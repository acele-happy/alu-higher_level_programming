#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # If the character is lowercase (ord('a') = 97 to ord('z') = 122)
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting 32 (difference between uppercase and lowercase ASCII values)
            print(chr(ord(char) - 32), end='')
        else:
            # If it's not lowercase, just print the character
            print(char, end='')
    print()  # New line after printing the string
