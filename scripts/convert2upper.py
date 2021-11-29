from Bio.Seq import Seq
from Bio import SeqIO
from Bio import SearchIO
from Bio.SeqRecord import SeqRecord

from Bio import AlignIO

import sys

records = list(SeqIO.parse(sys.argv[1], "fasta"))
outfilename = sys.argv[2]
new_records = []
for r in records:
    new_record = SeqRecord(r.seq.upper(), id=r.id, name=r.name, description = "")
    #new_record.letter_annotations["phred_quality"] = r.letter_annotations["phred_quality"]
    new_records.append(new_record)

with open(outfilename, "w") as output_handle:
     SeqIO.write(new_records, output_handle, "fasta")
