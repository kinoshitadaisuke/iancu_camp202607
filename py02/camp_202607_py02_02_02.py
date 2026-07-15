#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 16:09:50 (UT+08:00) daisuke>
#

# main function
def main ():
    # data file name
    file_data = 'hyperleda.data'
    # opening file for reading
    with open (file_data, 'r') as fh_in:
        # reading file line-by-line
        for line in fh_in:
            # skipping line if the line starts with '#'
            if (line[0] == '#'):
                continue
            # skipping line if the line starts with 'objname'
            if (line[:7] == 'objname'):
                continue
            # splitting line
            (objname, objtype, v_str, v_err_str, \
             modbest_str, modbest_err_str) = line.split (',')
            # converting string into float
            v           = float (v_str)
            v_err       = float (v_err_str)
            modbest     = float (modbest_str)
            modbest_err = float (modbest_err_str)
            # calculation of distance in Mpc
            d_Mpc = 10**(modbest / 5.0 - 5.0)
            # printing values
            print (f'{objname:32s}  {objtype:4s}  {d_Mpc:8.3f}  {v:15.3f}')
        

# executing main function
if (__name__ == '__main__'):
    main ()
