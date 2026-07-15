#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 14:30:19 (UT+08:00) daisuke>
#

# main function
def main ():
    # input file name
    file_input = 'line_01.data'
    # opening file for reading
    with open (file_input, 'r') as fh_in:
        # reading file line-by-line
        for line in fh_in:
            # splitting line
            (x_str, y_str) = line.split ()
            # converting string into float
            x = float (x_str)
            y = float (y_str)
            # printing x and y
            print (f'{x:5.2f} {y:5.2f}')

# executing the main function
if (__name__ == '__main__'):
    main ()
