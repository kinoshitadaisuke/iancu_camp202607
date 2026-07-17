#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 09:53:14 (UT+08:00) daisuke>
#

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = 'star_planet_1.bin'

    # reading a simulation from a file
    sim = rebound.Simulation (file_sim)

    # printing simulation object
    print (sim)

# execution of main function
if (__name__ == '__main__'):
    main ()
