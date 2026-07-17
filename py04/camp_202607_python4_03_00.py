#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 10:38:16 (UT+08:00) daisuke>
#

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = '3body_figure8.bin'

    # constructing a simulation object
    sim = rebound.Simulation ()

    #
    # Initial condition for figure-8 solution of 3-body problem
    #
    
    # star 1
    star1_m  = 1.0
    star1_x  = -0.97000436
    star1_y  = 0.24308753
    star1_z  = 0.0
    star1_vx = 0.46620531
    star1_vy = 0.43236573
    star1_vz = 0.0

    # star 2
    star2_m  = 1.0
    star2_x  = 0.97000436
    star2_y  = -0.24308753
    star2_z  = 0.0
    star2_vx = 0.46620531
    star2_vy = 0.43236573
    star2_vz = 0.0

    # star 3
    star3_m  = 1.0
    star3_x  = 0.0
    star3_y  = 0.0
    star3_z  = 0.0
    star3_vx = -0.93241062
    star3_vy = -0.86473146
    star3_vz = 0.0

    # adding stars
    sim.add (m=star1_m, \
             x=star1_x, y=star1_y, z=star1_z, \
             vx=star1_vx, vy=star1_vy, vz=star1_vz)
    sim.add (m=star2_m, \
             x=star2_x, y=star2_y, z=star2_z, \
             vx=star2_vx, vy=star2_vy, vz=star2_vz)
    sim.add (m=star3_m, \
             x=star3_x, y=star3_y, z=star3_z, \
             vx=star3_vx, vy=star3_vy, vz=star3_vz)

    # printing simulation object
    print (sim)

    # saving simulation into a file
    sim.save_to_file (file_sim)

# execution of main function
if (__name__ == '__main__'):
    main ()
