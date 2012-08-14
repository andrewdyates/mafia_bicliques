#!/usr/bin/python
"""Objects representing MAFIA output files."""

class MafiaBiclique(object):
  """Bicliques from MAFIA. Rows and columns indexed by zero.

  Note: In graph file, rows are indexed from 1, not zero. Items are indexed from 0.
  Correct this by subtracting one from every entry in rows.
  """
  def __init__(self, fp, n, missing_rows=None):
    n = int(n)
    assert fp and n > 0
    if missing_rows is None:
      self.missing_rows = set()
    else:
      self.missing_rows = set(missing_rows)
    self.bicliques = [] #rows, cols, density
    self.row_set, self.col_set = set(), set()
    self.row_map = make_row_map(n, self.missing_rows)
    self.bicliques = []
    
    for line in fp:
      rows, cols = [map(int, s.strip().split(' ')) for s in line.split(';')]
      rows = map(lambda x: self.row_map[x-1], rows) # remap rows
      self.row_set.update(rows)
      self.col_set.update(cols)
      self.bicliques.append((set(rows), set(cols)))
      
  def __str__(self):
    return "{{DensityMergedGraph: " + str(self.bicliques) + "}}"
  
  def yield_lines_to_density_merger(self):
    for rows, cols in self.bicliques:
      # index from 1
      yield " ".join(map(lambda x:str(x+1), rows)) + " ; " + " ".join(map(lambda x:str(x+1), cols)) + " \n"


class DensityMergedGraph(object):
  """Bicliques from `GraphMining` program. Indexed from 1, missing rows inserted.

  Note: In graph file, rows and cols are indexed from 1, not zero.
  Correct this by subtracting one from every entry.
  """
  def __init__(self, fp):
    self.bicliques = [] #rows, cols, density
    self.row_set = set()
    self.col_set = set()
    for line in fp:
      rows, cols, density = map(lambda s: s.strip().split(' '), line.split(';'))
      d={'rows': map(lambda x: int(x)-1, rows),
         'cols': map(lambda x: int(x)-1, cols),
         'density': float(density[1])}
      self.row_set.update(d['rows'])
      self.col_set.update(d['cols'])
      self.bicliques.append(d)
      
  def __str__(self):
    return "{{DensityMergedGraph: " + str(self.bicliques) + "}}"

  def remap(self, row_map, col_map):
    for d in self.bicliques:
      d['rows'] = [row_map[x] for x in d['rows']]
      d['cols'] = [col_map[x] for x in d['cols']]
    self.row_set = set([row_map[x] for x in self.row_set])
    self.col_set = set([col_map[x] for x in self.col_set])


def get_missing_set(fp):
  s = set([int(s.strip()) for s in fp])
  return s
  
def make_row_map(n, missing_rows):
  """Map row indices from a truncated row list to rows in the full n-row matrix.
  Indicies are from 0.

  Args:
    n: int of total number of rows
    missing_rows: set([int]) of missing row indices.
  """
  row_map = {}
  j = 0
  mapped = set()
  for i in xrange(n):
    if i not in missing_rows:
      row_map[j] = i
      j += 1
    else:
      mapped.add(i)
  assert len(row_map) + len(missing_rows) == n
  assert mapped == set(missing_rows)
  return row_map

