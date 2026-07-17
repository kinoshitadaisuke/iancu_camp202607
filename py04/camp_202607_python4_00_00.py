#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 09:52:13 (UT+08:00) daisuke>
#

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = 'star_planet_1.bin'

    # constructing a simulation object
    sim = rebound.Simulation ()

    # adding one solar mass star
    sim.add (m=1.0)

    # adding a planet of m=0.001, a=1, and e=0.0
    sim.add (m=10**-3, a=1.0, e=0.0)

    # printing simulation object
    print (sim)

    # saving simulation into a file
    sim.save_to_file (file_sim)

# execution of main function
if (__name__ == '__main__'):
    main ()
