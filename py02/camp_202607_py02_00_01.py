#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 14:26:52 (UT+08:00) daisuke>
#

# main function
def main ():
    # output file name
    file_output = 'line_01.data'
    # opening a file for writing
    with open (file_output, 'w') as fh_out:
        # for each x value
        for x in range (0, 10, 1):
            # y value
            y = 2.0 * x + 1.0
            # printing x and y value
            print (f'{x:5.2f} {y:5.2f}')
            # writing x and y value into file
            fh_out.write (f'{x:5.2f} {y:5.2f}\n')

# executing the main function
if (__name__ == '__main__'):
    main ()
