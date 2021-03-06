import sys
import re
import subprocess
import urllib.request
from Bio.Seq import Seq, transcribe, translate
from Bio.Align.Applications import MuscleCommandline
from Bio import SeqIO

if __name__ == '__main__':

    file_in = sys.argv[1]
    f_out = 'motif_sequence.fa'
    pattern = re.compile("KL[EI]{2,}K")
    muscle_exe = "muscle"
    in_file = f_out
    out_file = "out_motif_sequence.fa"


    if file_in[-3:] != '.fa':
        sys.exit('WARNING: only fasta format accepted')

    else:
        my_sequence_recorded = list(SeqIO.parse(open(file_in, mode='r'), 'fasta'))

    if (len(my_sequence_recorded)) == 0:
        sys.exit('WARNING: Empty file')

    else:

        my_sequence_recorded_motif = []
        for seq in my_sequence_recorded:
            for match in re.finditer(pattern, str(seq.seq)):
                my_sequence_recorded_motif += [seq]
                print('>' + seq.id)
                print(seq.seq)


