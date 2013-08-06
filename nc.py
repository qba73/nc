#!/usr/bin/env python
"""
File format converter.
The script converts csv file to netcdf format.

Limitations:
1) only for small csv files
2) csv files without header - csv module is not used!

"""

import sys
import os.path
import csv
import pupynere


def update_name(old_name):
    new = old_name.split('.')
    new[-1] = 'nc'
    return '.'.join(new)


def csv_to_nc(csvfl):
    """
    Transforms csv file into netcdf format.

    :Args:
      - csvfl cvs data file, example: data.csv

    :Returns:
      - netcdf file, example: data.nc
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


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: nc.py csvfile")
        raise SystemExit(1)

    if not os.path.exists(sys.argv[1]):
        print("Error: csvdata file {0} not found".format(sys.argv[1]))
        raise SystemExit(1)

    csv_to_nc(sys.argv[1])
   
