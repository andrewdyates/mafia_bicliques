#!/usr/bin/python
"""Convert graph row IDs into labels.

Example Use
"""
import sys
from geo_api.lite import *
import collections
from __init__ import *


def main(gpl_rows_file=None, gpl_rows_col=None, gpl_cols_file=None, gpl_cols_col=None, missing_rows_fname=None, graph_fname=None):
  assert gpl_rows_file and gpl_cols_file and missing_rows_fname and gpl_rows_col and gpl_cols_col and graph_fname
  # load GPLs
  gplrow, gplcol = GPL_Lite(gpl_rows_file), GPL_Lite(gpl_cols_file)
  # Load missing row numbers
  missing_rows = [int(s) for s in open(missing_rows_fname) if s]
  # load graph
  G = DensityMergedGraph(graph_fname)
  # map row ids in graph to gene symbols
  # output result
  print G


      
      


  
if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))

