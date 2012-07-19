#!/usr/bin/python
import sys
import json
from geo_api import *


def main(gpl1=None, gpl2=None):
  
  # load GPLs
  # load missing row numbers
  # load graph
  # map row ids in graph to gene symbols
  # output result
  pass

if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
