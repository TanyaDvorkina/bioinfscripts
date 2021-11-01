# bioinfscripts
Useful scripts to parse bioinformatics data

## Description

Converts De Bruijn graph in gfa-format into dot:
```
	python ./scripts/gfa2dot.py graph.gfa graph.dot [edge_colors.tsv] 
```

Filters reads by length
```
	python ./scripts/filter_by_length.py file.fasta min_len
```
