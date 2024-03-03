import sys

# Function to convert a decimal number to a given base from 2-16
def convert(num, base):

    if num < 0:
        print(" ".join(command))
        raise ValueError(f"{num} should be greater than 0. Exiting...")
        sys.exit(1)
    elif base not in range(2, 17):
        print(" ".join(command))
        raise ValueError(f"{base} should be between 2 and 16. Exiting...")
        sys.exit(1)

    print(f"Converting {num} to base {base}...")
    result = ""

    while num > 0:
        digit = num % base
        if digit < 10:
            result = str(digit) + result
        else:
            result = chr(ord("A") + digit - 10) + result
        num //= base

    return result if result else "0"

# Gather inputs (number and radix)
if __name__ == "__main__":

    # n must be > 0 and b must be between 2 and 16, inclusive
    global command
    command = sys.argv
    args = sys.argv[1:]
    
    if len(args) != 2:
        print("Usage: base_converter.py INTEGER RADIX")
        sys.exit(1)

    n, b = map(int, args)

    result = convert(n, b)
    print(f"{n} in base {b} is {result}.")