#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 10:13:07 (UT+08:00) daisuke>
#

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = 'sirius_system.bin'

    # constructing a simulation object
    sim = rebound.Simulation ()

    # adding Sirius A
    sim.add (m=2.063)

    # adding Sirius B
    sim.add (m=1.018, a=19.8, e=0.59142)

    # printing simulation object
    print (sim)

    # saving simulation into a file
    sim.save_to_file (file_sim)

# execution of main function
if (__name__ == '__main__'):
    main ()
