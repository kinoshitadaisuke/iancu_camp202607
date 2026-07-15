#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 14:24:59 (UT+08:00) daisuke>
#

# main function
def main ():
    # for each x value
    for x in range (0, 10, 1):
        # y value
        y = 2.0 * x + 1.0
        # printing x and y value
        print (f'{x:5.2f} {y:5.2f}')

# executing the main function
if (__name__ == '__main__'):
    main ()
