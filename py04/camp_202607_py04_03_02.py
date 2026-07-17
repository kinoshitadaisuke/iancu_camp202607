#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 10:40:57 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = '3body_figure8.bin'

    # name of output file
    file_output = '3body_figure8.data'

    # reading a simulation from a file
    sim = rebound.Simulation (file_sim)

    # printing simulation object
    print (sim)

    # moving to centre of momentum frame
    sim.move_to_com ()

    # particles in simulation
    ps = sim.particles

    # parameters for simulation
    #  for G=1, one year is equal to 2 pi
    #  0.01 time unit = 365.25 / (2 pi) * 0.01 = 0.58 day
    year       = 2.0 * numpy.pi
    t_interval = 0.01
    dt         = 0.001
    n_output   = 3000

    # settings for orbital integration
    sim.integrator = 'ias15'
    sim.dt         = dt

    # opening file for writing
    with open (file_output, 'w') as fh:
        # header of output file
        header = f"# year from start of simulation, particle 1 (x, y, z), particle 2 (x, y, z), ...\n"
        # writing header to output file
        fh.write (header)

        # orbital integration
        for i in range (n_output):
            # time
            t    = t_interval * i
            t_yr = t_interval * i / (2.0 * numpy.pi)
            # string for writing data to output file
            record = f'{t_yr:15.6f}'
            # orbital integration for a time step
            sim.integrate (t)
            # positions of particles
            for i in range (sim.N):
                x = ps[i].x
                y = ps[i].y
                z = ps[i].z
                # appending positions to string
                record += f':{x:15.6f},{y:15.6f},{z:15.6f}'
            # writing time and positions to output file
            fh.write (f'{record}\n')

# execution of main function
if (__name__ == '__main__'):
    main ()
