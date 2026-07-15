#!/usr/bin/env python3

#
# Time-stamp: <2026/07/15 15:57:25 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# main function
def main ():
    # allow insecure downloading
    ssl._create_default_https_context = ssl._create_unverified_context

    # URL of data file
    url_data = 'https://s3b.astro.ncu.edu.tw/camp_202607/data/hyperleda.data'

    # output file name
    file_output = 'hyperleda.data'

    # printing status
    print (f'Now, fetching {url_data}...')

    # making a request object
    req = urllib.request.Request (url_data)
    req.add_header ('User-Agent', 'Mozilla/5.0')
    
    # opening URL
    with urllib.request.urlopen (req) as fh_read:
        # reading data
        data_byte = fh_read.read ()
	    
    # printing status
    print (f'Finished fetching {url_data}!')
        
    # printing status
    print (f'Now, writing data into file "{file_output}"...')
    
    # opening file for writing
    with open (file_output, 'wb') as fh_write:
        # writing data
        fh_write.write (data_byte)

    # printing status
    print (f'Finished writing data into file "{file_output}"!')

# execution of main function
if (__name__ == '__main__'):
    main ()
