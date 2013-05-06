#!/usr/bin/env python
"""
File format converter.
The script converts csv file to netcdf format.

Limitations:
1) only for small csv files
2) csv files without header - csv module is not used!

The script is based on code from the following blog post:
http://www.j-raedler.de/2010/12/how-to-convert-a-csv-file-\
to-netcdf-with-7-lines-of-python-code/

Dependencies:

1) numpy
2) pupynere

"""

import sys
import os.path
import pupynere


def update_name(old_name):
    new = old_name.split('.')
    new[-1] = 'nc'
    return '.'.join(new)


def csv_to_nc(argv):
    """Transform csv file into netcdf format.

    Args:
      - argv: filename, example: data.csv

    Returns:
      - netcdf file, example: data.nc

    Usage:
      $ ./csv_to_nc.py data.csv

    """
    with open(sys.argv[1], 'r') as f:
        ll = [l.strip().split(',') for l in 
              f.readlines() if not l.startswith('#')]

    vv = zip(*[map(float, l) for l in ll])

    transformed_file = update_name(sys.argv[1])
    nc = pupynere.netcdf_file(transformed_file, 'w')

    nc.createDimension('dim', None)

    for i, item in enumerate(vv):
       nc.createVariable('var_%02d' % i, 'd', ('dim',))[:] = vv[i]
    return 0


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: {0} <data_file.csv>".format(argv[0]))
	return 1

    if not os.path.exists(argv[1]):
        sys.stderr.write("ERROR: csv data file {0} not found.".format(argv[1]))
	return 1

    return csv_to_nc(argv)


if __name__ == "__main__": 
    sys.exit(main(sys.argv))
