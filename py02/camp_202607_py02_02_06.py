#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 17:12:57 (UT+08:00) daisuke>
#

# Hubble constant in km/sec/Mpc
H0 = 66.517

# 1 parsec
pc = 3.086 * 10**16

# Hubble constant in 1/sec
H0_SI = H0 * 10**3 / (pc * 10**6)

# Hubble time in sec
HubbleTime_sec = 1.0 / H0_SI

# Hubble time in yr
HubbleTime_yr = HubbleTime_sec / (365.25 * 24 * 3600)

# printing Hubble time in yr
print (f'Hubble Time = {HubbleTime_yr} yr')
print (f'            = {HubbleTime_yr / 10**9} Gyr')
