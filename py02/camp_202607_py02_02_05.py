#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 17:12:17 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# a function for straight line
def linear (x, a):
    # line
    y = a * x
    # returning y
    return (y)

# main function
def main ():
    # data file name
    file_data = 'hyperleda_dv.data'
    # output file name
    file_output = 'hyperleda_hd2.png'
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

    #
    # carrying out least-square method
    #

    # initial guess of coefficients
    param0 = [1.0]

    # least-squares fitting
    popt, pcov = scipy.optimize.curve_fit (linear, data_d, data_v, \
                                           p0=param0)

    # result of fitting
    print (f'popt:\n{popt}')
    print (f'pcov:\n{pcov}')

    # fitted a
    a_fitted = popt[0]

    # degree of freedom
    dof = len (data_d) - len (popt)
    print (f'dof = {dof}')

        # reduced chi-squared
    residual     = data_v - linear (data_d, a_fitted)
    reduced_chi2 = (residual**2).sum () / dof
    print (f'reduced chi-squared = {reduced_chi2}')

    # fitted a
    a_err = numpy.sqrt ( numpy.diagonal (pcov) )
    print (f'a = {a_fitted:8.3f} +/- {a_err[0]:8.3f} ({a_err[0]/a_fitted*100.0:8.3f}%)')

    # fitted line
    d_min    = 0.0
    d_max    = 500.0
    fitted_d = numpy.linspace (d_min, d_max, 1000)
    fitted_v = linear (fitted_d, a_fitted)
    
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
    ax.plot (fitted_d, fitted_v, \
             linestyle='--', linewidth=3.0, color='red', \
             label='line fitting result')
    ax.legend ()

    # saving a plot as a file
    fig.savefig (file_output, dpi=225.0)

# executing main function
if (__name__ == '__main__'):
    main ()
