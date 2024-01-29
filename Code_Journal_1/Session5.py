import numpy as np
from tabulate import tabulate
# Write a Python program that writes out a table of the function sin(x)
# vs. x, where x is tabulated between 0 and 2 with a thousand entries.
# Follow the basic Python program structure, including a main program
# function.

def main():
    x_values = np.arange(0, 2.002,  2/1000)
    sin_list = []

    for x in x_values:
        sin_list.append((x, np.sin(x)))



    table_headers = [f"sin(x)", "y"]
    print(tabulate(sin_list, headers=table_headers, floatfmt=".3f"))



if __name__ == "__main__":
    main()