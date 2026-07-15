#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 14:56:35 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# a function for straight line
def linear (x, a, b):
    # line
    y = a * x + b
    # returning y
    return (y)

# main function
def main ():
    # input file name
    file_input = 'line_01.data'
    # output file name
    file_output = 'line_01b.png'
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

    #
    # carrying out least-square method
    #

    # initial guess of coefficients
    param0 = [1.0, 1.0]

    # least-squares fitting
    popt, pcov = scipy.optimize.curve_fit (linear, data_x, data_y, \
                                           p0=param0)

    # result of fitting
    print (f'popt:\n{popt}')
    print (f'pcov:\n{pcov}')

    # fitted a and b
    a_fitted, b_fitted = popt

    # degree of freedom
    dof = len (data_x) - len (popt)
    print (f'dof = {dof}')

    # reduced chi-squared
    residual     = data_y - linear (data_x, a_fitted, b_fitted)
    reduced_chi2 = (residual**2).sum () / dof
    print (f'reduced chi-squared = {reduced_chi2}')

    # fitted a and b
    a_err, b_err = numpy.sqrt ( numpy.diagonal (pcov) )
    print (f'a = {a_fitted:8.3f} +/- {a_err:8.3f} ({a_err/a_fitted*100.0:8.3f}%)')
    print (f'b = {b_fitted:8.3f} +/- {b_err:8.3f} ({b_err/b_fitted*100.0:8.3f}%)')

    # fitted line
    x_min    = -1.0
    x_max    = 10.0
    fitted_x = numpy.linspace (x_min, x_max, 1000)
    fitted_y = linear (fitted_x, a_fitted, b_fitted)

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
             zorder=0.2, \
             label='sample data for least-square method')
    ax.plot (fitted_x, fitted_y, \
             linestyle='--', linewidth=2.0, color='red', \
             zorder=0.1, \
             label='fitted line by least-square method')
    ax.legend ()

    # saving a plot as a file
    fig.savefig (file_output, dpi=225.0)

# executing the main function
if (__name__ == '__main__'):
    main ()
