#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 15:21:30 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# a function for straight line
def linear (x, a, b):
    # line
    y = a * x + b
    # returning y
    return (y)

# main function
def main ():
    # output file name
    file_output = 'line_02.data'
    # values of x
    data_x = numpy.linspace (0.0, 10.0, 11)
    # values of y
    a      = 2.0
    b      = 1.0
    data_y = linear (data_x, a, b)
    # initialising random number generator
    rng = numpy.random.default_rng ()
    # opening a file for writing
    with open (file_output, 'w') as fh_out:
        # for each x value
        for i in range (len (data_x)):
            # generating a random number of Gaussian distribution
            rn = rng.normal (loc=0.0, scale=0.3, size=1)
            # printing x and y value
            print (f'{data_x[i]:5.2f} {data_y[i]+rn[0]:5.2f}')
            # writing x and y value into file
            fh_out.write (f'{data_x[i]:5.2f} {data_y[i]+rn[0]:5.2f}\n')

# executing the main function
if (__name__ == '__main__'):
    main ()
