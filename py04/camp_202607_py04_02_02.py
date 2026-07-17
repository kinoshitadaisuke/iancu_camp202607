#!/usr/bin/env python3

#
# Time-stamp: <2026/07/16 10:23:03 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = 'sirius_system.bin'

    # name of output file
    file_output = 'sirius_system.data'

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
    t_interval = 0.5
    dt         = 0.05
    n_output   = 2000

    # settings for orbital integration
    sim.integrator = 'ias15'
    sim.dt         = dt

    # opening file for writing
    with open (file_output, 'w') as fh:
        # header of output file
        header = f"# year from start of simulation, Sirius A (x, y, z), Sirius B (x, y, z)\n"
        # writing header to file
        fh.write (header)

        # orbital integration
        for i in range (n_output):
            # time
            t     = t_interval * i
            t_day = t_interval * i * 365.25 / (2.0 * numpy.pi)
            t_yr  = t_interval * i / (2.0 * numpy.pi)
            # orbital integration for a time step
            sim.integrate (t)
            # position of Sirius A at time t
            a_x = ps[0].x
            a_y = ps[0].y
            a_z = ps[0].z
            # position of Sirius B at time t
            b_x = ps[1].x
            b_y = ps[1].y
            b_z = ps[1].z
            # position of Sirius A and B at time t
            record = f"{t_yr:12.6f}" \
                + f" {a_x:+12.6f} {a_y:+12.6f} {a_z:+12.6f}" \
                + f"{b_x:+12.6f} {b_y:+12.6f} {b_z:+12.6f}\n"
            # writing position of Sirius A and B to file
            fh.write (record)

# execution of main function
if (__name__ == '__main__'):
    main ()
