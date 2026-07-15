#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 15:19:29 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# main function
def main ():
    # input file name
    file_input = 'line_02.data'
    # output file name
    file_output = 'line_02a.png'
    # making empty lists for storing data
    list_x = []
    list_y = []
    # opening file for reading
    with open (file_input, 'r') as fh_in:
        # reading file line-by-line
        for line in fh_in:
            # splitting line
            (x_str, y_str) = line.split ()
            # converting string into float
            x = float (x_str)
            y = float (y_str)
            # appending x and y to the end of lists
            list_x.append (x)
            list_y.append (y)
    # printing list_x and list_y
    print (f'{list_x}')
    print (f'{list_y}')
    # making numpy arrays
    data_x = numpy.array (list_x)
    data_y = numpy.array (list_y)
    
    # making fig, canvas, and ax objects for plotting
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111)

    # settings for axes
    ax.set_xlabel ('$x$')
    ax.set_ylabel ('$y$')
    ax.set_xlim (-2.0, +12.0)
    ax.set_ylim (-2.0, +22.0)
    ax.grid ()

    # plotting data
    ax.plot (data_x, data_y, \
             linestyle='None', marker='o', markersize=3.0, color='blue', \
             label='sample data for least-square method')
    ax.legend ()

    # saving a plot as a file
    fig.savefig (file_output, dpi=225.0)

# executing the main function
if (__name__ == '__main__'):
    main ()
