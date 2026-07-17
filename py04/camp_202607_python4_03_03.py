#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 10:42:14 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# main function
def main ():
    # name of input data file
    file_data = '3body_figure8.data'

    # name of directory for storing PNG files
    dir_png = '3body_figure8'

    # making directory if not exist
    path_dir_png = pathlib.Path (dir_png)
    if not (path_dir_png.exists ()):
        path_dir_png.mkdir ()

    # figure file name prefix
    prefix_fig = '3body_figure8'

    # counter
    i = 0

    # opening data file for reading
    with open (file_data, 'r') as fh:
        # reading data file
        for line in fh:
            # skipping line if the line starts with '#'
            if (line[0] == '#'):
                continue
            # splitting line
            data = line.split (':')
            # figure file name
            file_fig = f"{dir_png}/{prefix_fig}_{i:08d}.png"
            
            # making objects "fig", "canvas", and "ax"
            fig    = matplotlib.figure.Figure ()
            canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
            ax     = fig.add_subplot (111)
            
            # labels
            ax.set_xlabel ('X')
            ax.set_ylabel ('Y')

            # axes
            ax.set_xlim (-1.5, +1.5)
            ax.set_ylim (-1.5, +1.5)
            ax.set_aspect ('equal')
            ax.grid ()

            # number of particles
            n_particles = (len (data) - 1) // 2
            
            # plotting locations of particles
            for j in range (len (data)):
                if (j == 0):
                    continue
                (x_str, y_str, z_str) = data[j].split (',')
                x = float (x_str)
                y = float (y_str)
                z = float (z_str)
                if (j == 1):
                    ax.plot (x, y, \
                             linestyle='None', marker='o', markersize=5, \
                             color='red')
                if (j == 2):
                    ax.plot (x, y, \
                             linestyle='None', marker='o', markersize=5, \
                             color='green')
                if (j == 3):
                    ax.plot (x, y, \
                             linestyle='None', marker='o', markersize=5, \
                             color='blue')
            
            # title
            ax.set_title (f"Figure-8 solution of 3 body problem")
            
            # saving the plot into a file
            fig.tight_layout ()
            fig.savefig (file_fig, dpi=225)
            
            # incrementing counter
            i += 1
         
# execution of main function
if (__name__ == '__main__'):
    main ()
