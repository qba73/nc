#!/usr/bin/env python
"""
File format converter.
The script converts csv file to netcdf format.
"""

import os.path
import pupynere


def new_name(old_name):
    '''Return filename with new ext nc'''
    return '.'.join([os.path.splitext(old_name)[0], 'nc'])


def read_file(fl):
    '''Yields csv line

    :Args:
      - fl, csv file for transformation

    '''
    with open(fl, 'r') as f:
        for line in f:
            if not line.startswith('#'):
                yield line.strip().split(',')


def make_float(fl):
    '''Returns generator that yields csv lines with float numbers

    :Args:
     - fl, csv file for transformation

    '''
    return (item for item in zip(*[map(float, l) for l in read_file(fl)]))


def transform(fl):
    """Transforms csv file into netcdf format.

    :Args:
      - fl, cvs data file, example: data.csv

    :Returns:
      - netcdf file, example: data.nc

    """
    nc = pupynere.netcdf_file(new_name(fl), 'w')
    nc.createDimension('dim', None)

    for i, item in enumerate(make_float(fl)):
        nc.createVariable('var_%02d' % i, 'd', ('dim',))[:] = item


def main():
    import sys
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: csvnc <csvfile>\n")
        raise SystemExit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Error: csvdata file {0} not found\n".format(
            sys.argv[1]))
        raise SystemExit(1)

    transform(sys.argv[1])


if __name__ == "__main__":
    main()
