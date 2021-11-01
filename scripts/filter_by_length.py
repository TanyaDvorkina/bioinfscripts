from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqIO import FastaIO
from Bio import SearchIO
from Bio.SeqRecord import SeqRecord

import sys
from pathlib import Path

filename = Path(sys.argv[1])
min_len = int(sys.argv[2])
lst = []
for r in SeqIO.parse(filename, "fasta"):
    if len(r.seq) > min_len:
         lst.append(r)

with open(filename.with_suffix("." + str(min_len) + ".fa"), "w") as output_handle:
    fasta_out = FastaIO.FastaWriter(output_handle, wrap=None)
    fasta_out.write_file(lst)


