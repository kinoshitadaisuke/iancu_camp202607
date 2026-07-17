#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 10:38:43 (UT+08:00) daisuke>
#

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = '3body_figure8.bin'

    # reading a simulation from a file
    sim = rebound.Simulation (file_sim)

    # printing simulation object
    print (sim)

# execution of main function
if (__name__ == '__main__'):
    main ()
