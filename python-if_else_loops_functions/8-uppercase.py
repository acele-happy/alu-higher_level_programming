#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # If the character is lowercase (ord('a') = 97 to ord('z') = 122)
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting 32 (difference between uppercase and lowercase ASCII values)
            result += chr(ord(char) - 32)
        else:
            # If it's not lowercase, just add the character as is
            result += char
    
    # Print the final result using string format
    print("{}".format(result))
