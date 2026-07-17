#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 21:33:17 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing rebound module
import rebound

# main function
def main ():
    # output file name
    file_sim = 'galaxy_collision_1.bin'
    
    # particles in galaxy
    gal1_particles = [
        {
            'r': 0.0,       # radius
            'm': 1.0*10**9, # mass
            'n': 1,         # number of particles
        },
        {
            'r': 1.0*10**3,
            'm': 100.0,
            'n': 8,
        },
        {
            'r': 2.0*10**3,
            'm': 100.0,
            'n': 16,
        },
        {
            'r': 3.0*10**3,
            'm': 100.0,
            'n': 24,
        },
        {
            'r': 4.0*10**3,
            'm': 100.0,
            'n': 32,
        },
        {
            'r': 5.0*10**3,
            'm': 100.0,
            'n': 40,
        },
        {
            'r': 6.0*10**3,
            'm': 100.0,
            'n': 48,
        },
        {
            'r': 7.0*10**3,
            'm': 100.0,
            'n': 56,
        },
        {
            'r': 8.0*10**3,
            'm': 100.0,
            'n': 64,
        },
        {
            'r': 9.0*10**3,
            'm': 100.0,
            'n': 72,
        },
        {
            'r': 10.0*10**3,
            'm': 100.0,
            'n': 80,
        },
        {
            'r': 11.0*10**3,
            'm': 100.0,
            'n': 88,
        },
        {
            'r': 12.0*10**3,
            'm': 100.0,
            'n': 96,
        },
        {
            'r': 13.0*10**3,
            'm': 100.0,
            'n': 104,
        },
        {
            'r': 14.0*10**3,
            'm': 100.0,
            'n': 112,
        },
        {
            'r': 15.0*10**3,
            'm': 100.0,
            'n': 120,
        },
        {
            'r': 16.0*10**3,
            'm': 100.0,
            'n': 128,
        },
        {
            'r': 17.0*10**3,
            'm': 100.0,
            'n': 136,
        },
        {
            'r': 18.0*10**3,
            'm': 100.0,
            'n': 144,
        },
        {
            'r': 19.0*10**3,
            'm': 100.0,
            'n': 152,
        },
        {
            'r': 20.0*10**3,
            'm': 100.0,
            'n': 160,
        },
    ]
    # making a new simulation
    sim = rebound.Simulation ()
    # moving to centre of momentum frame
    sim.move_to_com ()
    # adding particles to simulation
    for ring in gal1_particles:
        for i in range (ring['n']):
            theta = i / ring['n'] * 2.0 * numpy.pi
            x = ring['r'] * numpy.cos (theta)
            y = ring['r'] * numpy.sin (theta)
            z = 0.0
            if (ring['r'] == 0.0):
                v = 0.0
            else:
                v = numpy.sqrt (gal1_particles[0]['m'] / ring['r'])
            vx = -1.0 * v * numpy.sin (theta)
            vy = +1.0 * v * numpy.cos (theta)
            vz = 0.0
            sim.add (m=ring['m'], x=x, y=y, z=z, vx=vx, vy=vy, vz=vz)
    # printing simulation object
    print (sim)
    # saving simulation into a file
    sim.save_to_file (file_sim)
            

# execution of the main function
if (__name__ == '__main__'):
    main ()
