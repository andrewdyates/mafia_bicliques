#!/usr/bin/python

class DensityMergedGraph(object):
  """Bicliques from MAFIA.

  Note: In graph file, rows are indexed from 1, not zero. Items are indexed from 0.
  Correct this by subtracting one from every entry in rows.
  """
  def __init__(self, fp):
    self.bicliques = [] #rows, cols, density
    for line in fp:
      rows, cols, density = map(lambda s: s.strip().split(' '), line.split(';'))
      self.bicliques.append(
        {'rows': map(lambda x: int(x)-1, rows),
         'cols': map(int, cols),
         'density': float(density[1])}
        )
    fp.close()

    
  def __str__(self):
    return "{{DensityMergedGraph: " + str(self.bicliques) + "}}"
