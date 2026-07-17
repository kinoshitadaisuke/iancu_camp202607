#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 18:15:54 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing rebound module
import rebound

# main function
def main ():
    # simulation file
    file_sim = 'galaxy_collision_3.bin'
    # output file
    file_output = 'galaxy_collision_3.data'

    # loading simulation
    sim = rebound.Simulation (file_sim)

    # printing simulation object
    print (sim)

    # particles in simulation
    ps = sim.particles

    # parameters for simulation
    #  for G=1, one year is equal to 2 pi
    #  1 time unit = 365.25 / (2 pi) = 58 day
    year       = 2.0 * numpy.pi
    t_interval = 10.0
    n_output   = 2000
    dt         = 1.0
    
    # settings for orbital integration
#    sim.integrator = 'ias15'
    sim.integrator = 'whfast'
    sim.dt         = dt
    sim.softening  = 1.0
#    sim.N_active   = 2

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
            for j in range (sim.N):
                x = ps[j].x
                y = ps[j].y
                z = ps[j].z
                # appending positions to string
                record += f':{x:18.6f},{y:18.6f},{z:18.6f}'
            # writing time and positions to output file
            print (f't_yr = {t_yr} yr...')
            fh.write (f'{record}\n')
    
# execution of main function
if (__name__ == '__main__'):
    main ()
    
