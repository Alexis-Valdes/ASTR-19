import numpy as np

# Write a Python program that writes out a table of the function sin(x)
# vs. x, where x is tabulated between 0 and 2 with a thousand entries.
# Follow the basic Python program structure, including a main program
# function.

def main():
    x_values = np.arange(0, 2.002,  2/1000)

    print('|   x   |    sin(x)   |   y   |')
    for x in x_values:
        print(f"|   {x}    |   sin({x})    |   {np.sin(x):12}  |")


if __name__ == "__main__":
    main()