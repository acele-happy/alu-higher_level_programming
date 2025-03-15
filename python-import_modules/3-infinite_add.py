#!/usr/bin/python3
import sys
if __name__ == "__main__":
    # Start with a sum of 0
    total = 0
    # Iterate through each argument (skip the script name, so start from index 1)
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert the argument to an integer and add it to the total
    # Print the total sum
    print(total)
