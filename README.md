mafia_bicliques
===============

Map output from [Yang et al. MAFIA-MFI-DensityMerge](http://link.springer.com/article/10.1007/s13721-012-0009-3?null)
back to original matrix symbols. Handles indexing differences due to filtered rows and index-to-symbol
assignment as declared in GEO GPL platform file definitions.

This module does _not_ compute bicliques.

### Notable Objects ###
* MafiaBiclique: object representing MMAFIA-MFI output
* DensityMergedGraph: object representing GraphMerge output

### Example Use (stand alone script) ###
python $HOME/mafia_bicliques/script.py gpl_rows_file=$HOME/GPL8178.txt gpl_rows_col=miRNA_ID gpl_cols_file=$HOME/GPL6104.txt gpl_cols_col=Symbol missing_rows_fname=$HOME/gpl8178_gpl6104_spearman_-0.6_missing.txt graph_fname=$HOME/gpl8178_gpl6104_spearman_-0.6_0.05_fci.output

### Run Tests ###
    python test.py

  

