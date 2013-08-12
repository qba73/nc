#!/usr/bin/env python
"""
File format converter.
The script converts csv file to netcdf format.

"""

import os.path
import pupynere


def update_name(old_name):
    '''Return filename with new ext nc'''
    return '.'.join([os.path.splitext(old_name)[0], 'nc'])


def read_file(fl):
    '''Yields line by line

    :Args:
      - fl, csv file for transformation
    '''
    with open(fl, 'r') as f:
        for line in f:
            if not line.startswith('#'):
                yield line.strip().split(',')


def csv_to_nc(csvfl):
    """
    Transforms csv file into netcdf format.

    :Args:
      - csvfl cvs data file, example: data.csv

    :Returns:
      - netcdf file, example: data.nc
    """

    vv = (item for item in zip(*[map(float, l) for l in read_file(csvfl)]))

    transformed_file = update_name(csvfl)
    nc = pupynere.netcdf_file(transformed_file, 'w')

    nc.createDimension('dim', None)

    for i, item in enumerate(vv):
        nc.createVariable('var_%02d' % i, 'd', ('dim',))[:] = item
    return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: csvnc.py csvfile\n")
        raise SystemExit(1)

    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Error: csvdata file {0} not found\n".format(
            sys.argv[1]))
        raise SystemExit(1)

    csv_to_nc(sys.argv[1])