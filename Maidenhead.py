#!/usr/bin/env python
import mlocs

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('loc',help='Maidenhead grid or lat lon',nargs='+')
p.add_argument('-p','--precision',help='maidenhead precision',type=int,default=6)
p = p.parse_args()



if len(p.loc) == 1: #maidenhead
    lat,lon = mlocs.toLoc(p.loc[0])
    print(lat,lon)
elif len(p.loc) == 2: #lat lon
    maidenhead = mlocs.toMaiden(p.loc, p.precision)
    print(maidenhead)
else:
    raise TypeError('specify Maidenhead grid (single string) or lat lon (with space between)')