#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 17:06:37 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# main function
def main ():
    # data file name
    file_data = 'hyperleda_dv.data'
    # output file name
    file_output = 'hyperleda_hd1.png'
    # making empty lists for storing data
    list_d = []
    list_v = []
    # opening file for reading
    with open (file_data, 'r') as fh_in:
        # reading file line-by-line
        for line in fh_in:
            # splitting line
            (d_str, v_str) = line.split ()
            # converting string into float
            d = float (d_str)
            v = float (v_str)
            # appending data to lists
            if (d < 500.0):
                list_d.append (d)
                list_v.append (v)

    # making numpy arrays
    data_d = numpy.array (list_d)
    data_v = numpy.array (list_v)

    # making fig, canvas, and ax objects for plotting
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111)

    # settings for axes
    ax.set_xlabel ('$Distance [Mpc]$')
    ax.set_ylabel ('$Velocity [km/s]$')
    ax.grid ()

    # plotting data
    ax.plot (data_d, data_v, \
             linestyle='None', marker='o', markersize=1.0, color='blue', \
             label='data from HyperLEDA')
    ax.legend ()

    # saving a plot as a file
    fig.savefig (file_output, dpi=225.0)

# executing main function
if (__name__ == '__main__'):
    main ()
