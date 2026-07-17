#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 10:29:50 (UT+08:00) daisuke>
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
    file_data = 'sirius_system.data'

    # name of directory for storing PNG files
    dir_png = 'sirius_system'

    # making directory if not exist
    path_dir_png = pathlib.Path (dir_png)
    if not (path_dir_png.exists ()):
        path_dir_png.mkdir ()

    # figure file name prefix
    prefix_fig = 'sirius_system'

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
            (time, star_x, star_y, star_z, planet_x, planet_y, planet_z) \
                = line.split ()
            # figure file name
            file_fig = f"{dir_png}/{prefix_fig}_{i:08d}.png"
            
            # making objects "fig", "canvas", and "ax"
            fig    = matplotlib.figure.Figure ()
            canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
            ax     = fig.add_subplot (111)

            # labels
            ax.set_xlabel ('X [au]')
            ax.set_ylabel ('Y [au]')

            # axes
            ax.set_xlim (-25.0, +25.0)
            ax.set_ylim (-25.0, +25.0)
            ax.set_aspect ('equal')
            ax.grid ()

            # plotting location of star
            ax.plot (float (star_x), float (star_y), linestyle='None', \
                     marker='o', markersize=10, color='red', label='Sirius A')
            
            # plotting location of planet
            ax.plot (float (planet_x), float (planet_y), linestyle='None', \
                     marker='o', markersize=10, color='blue', label='Sirius B')

            # title
            ax.set_title (f"Sirius system at {float (time):6.2f} yr")
            
            # legend
            ax.legend (loc='upper right')
            
            # saving the plot into a file
            fig.savefig (file_fig, dpi=225)
            
            # incrementing counter
            i += 1
            
# execution of main function
if (__name__ == '__main__'):
    main ()
