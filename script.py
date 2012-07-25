#!/usr/bin/python
"""Convert graph row IDs into labels.

EXAMPLE USE:

python $HOME/mafia_bicliques/script.py gpl_rows_file=$HOME/GPL8178.txt gpl_rows_col=miRNA_ID gpl_cols_file=$HOME/GPL6104.txt gpl_cols_col=Symbol missing_rows_fname=$HOME/gpl8178_gpl6104_spearman_-0.6_missing.txt graph_fname=$HOME/gpl8178_gpl6104_spearman_-0.6_0.05_fci.output
"""
import sys
from geo_api.lite import *
from __init__ import *


def main(gpl_rows_file=None, gpl_rows_col=None, gpl_cols_file=None, gpl_cols_col=None, missing_rows_fname=None, graph_fname=None):
  #assert gpl_rows_file and gpl_cols_file and missing_rows_fname and gpl_rows_col and gpl_cols_col and graph_fname
  
  gplrow, gplcol = GPL_Lite(gpl_rows_file), GPL_Lite(gpl_cols_file)
  row_syms = gplrow.get_col_list(gpl_rows_col)
  col_syms = gplcol.get_col_list(gpl_cols_col)
    
  missing_rows = set([int(s) for s in open(missing_rows_fname) if s])
  
  G = DensityMergedGraph(open(graph_fname))
  # map row ids in graph to gene symbols
  row_map = make_row_map(len(gplrow.rows), missing_rows)

  for biclique in G.bicliques:
    row_nums = map(row_map.get, biclique['rows'])
    a = [row_syms[x] for x in row_nums]
    col_nums = biclique['cols']
    b = [col_syms[x] for x in col_nums]
    print "\t".join(a)
    print "\t".join(b)
    print "Rows: %d, Cols: %d, Density: %.2f" % (len(a), len(b), biclique['density'])
    print 
      
      


  
if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))

