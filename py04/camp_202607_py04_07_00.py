#!/usr/bin/env python3

#
# Time-stamp: <2026/07/17 08:59:39 (UT+08:00) daisuke>
#

# importing copy module
import copy

# importing numpy module
import numpy

# importing rebound module
import rebound

# main function
def main ():
    # output file name
    file_sim = 'galaxy_collision_4.bin'
    
    # particles in galaxy
    gal1_particles = [
        {
            'r': 0.0,       # radius
            'm': 1.0*10**6, # mass
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
        {
            'r': 21.0*10**3,
            'm': 100.0,
            'n': 168,
        },
        {
            'r': 22.0*10**3,
            'm': 100.0,
            'n': 176,
        },
        {
            'r': 23.0*10**3,
            'm': 100.0,
            'n': 184,
        },
        {
            'r': 24.0*10**3,
            'm': 100.0,
            'n': 192,
        },
        {
            'r': 25.0*10**3,
            'm': 100.0,
            'n': 200,
        },
    ]

    # making one more galaxy
    gal2_particles = copy.deepcopy (gal1_particles)

    # position offset of galaxy 1
    gal1_offset_x = -30000.0
    gal1_offset_y = -26000.0
    gal1_offset_z = +0.0
    # position offset of galaxy 2
    gal2_offset_x = +30000.0
    gal2_offset_y = +26000.0
    gal2_offset_z = +0.0
    # velocity of galaxy 1
    gal1_velocity_x = +10.0
    gal1_velocity_y = +0.0
    gal1_velocity_z = +0.0
    # velocity of galaxy 2
    gal2_velocity_x = -10.0
    gal2_velocity_y = +0.0
    gal2_velocity_z = +0.0
    
    # making a new simulation
    sim = rebound.Simulation ()
    # adding particles to simulation
    sim.add (m=gal1_particles[0]['m'], \
             x=gal1_offset_x, y=gal1_offset_y, z=gal1_offset_z, \
             vx=gal1_velocity_x, vy=gal1_velocity_y, vz=gal1_velocity_z)
    sim.add (m=gal2_particles[0]['m'], \
             x=gal2_offset_x, y=gal2_offset_y, z=gal2_offset_z, \
             vx=gal2_velocity_x, vy=gal2_velocity_y, vz=gal2_velocity_z)
    for ring in gal1_particles[1:]:
        for i in range (ring['n']):
            theta = i / ring['n'] * 2.0 * numpy.pi
            x = ring['r'] * numpy.cos (theta) + gal1_offset_x
            y = ring['r'] * numpy.sin (theta) + gal1_offset_y
            z = 0.0 + gal1_offset_z
            if (ring['r'] == 0.0):
                v = 0.0
            else:
                v = numpy.sqrt (gal1_particles[0]['m'] / ring['r'])
            vx = -1.0 * v * numpy.sin (theta) + gal1_velocity_x
            vy = +1.0 * v * numpy.cos (theta) + gal1_velocity_y
            vz = 0.0 + gal1_velocity_z
            sim.add (m=ring['m'], x=x, y=y, z=z, vx=vx, vy=vy, vz=vz)
    for ring in gal2_particles[1:]:
        for i in range (ring['n']):
            theta = i / ring['n'] * 2.0 * numpy.pi
            x = ring['r'] * numpy.cos (theta) + gal2_offset_x
            y = ring['r'] * numpy.sin (theta) + gal2_offset_y
            z = 0.0 + gal2_offset_z
            if (ring['r'] == 0.0):
                v = 0.0
            else:
                v = numpy.sqrt (gal2_particles[0]['m'] / ring['r'])
            vx = -1.0 * v * numpy.sin (theta) + gal2_velocity_x
            vy = +1.0 * v * numpy.cos (theta) + gal2_velocity_y
            vz = 0.0 + gal2_velocity_z
            sim.add (m=ring['m'], x=x, y=y, z=z, vx=vx, vy=vy, vz=vz)
    # moving to centre of momentum frame
    sim.move_to_com ()
    # printing simulation object
    print (sim)
    # saving simulation into a file
    sim.save_to_file (file_sim)
            

# execution of the main function
if (__name__ == '__main__'):
    main ()
