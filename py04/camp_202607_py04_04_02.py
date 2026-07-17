#!/usr/bin/env python3

#
# Time-stamp: <2026/07/17 08:52:04 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# main function
def main ():
    # data file name
    file_data = 'galaxy_collision_1.data'

    # name of directory for storing PNG files
    dir_png = 'galaxy_collision_1'

    # making directory if not exist
    path_dir_png = pathlib.Path (dir_png)
    if not (path_dir_png.exists ()):
        path_dir_png.mkdir ()
        
    # figure file name prefix
    prefix_fig = 'galaxy_collision_1'
    
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
            ax.set_xlim (-40000.0, +40000.0)
            ax.set_ylim (-40000.0, +40000.0)
            ax.set_aspect ('equal')
            ax.grid ()

            # plotting locations of particles
            for j in range (1, len (data)):
                (x_str, y_str, z_str) = data[j].split (',')
                x = float (x_str)
                y = float (y_str)
                z = float (z_str)
                if (j == 1):
                    ax.plot (x, y, \
                             linestyle='None', marker='o', markersize=5, \
                             color='red')
                else:
                    ax.plot (x, y, \
                             linestyle='None', marker='.', markersize=1, \
                             color='magenta')
            
            # title
            ax.set_title (f"A galaxy")
            
            # saving the plot into a file
            fig.savefig (file_fig, dpi=225)
            
            # incrementing counter
            i += 1

if (__name__ == '__main__'):
    main ()
