from Bio import SeqIO
from Bio.Seq import Seq, transcribe, translate
import sys

file_out='gene_seq_out.fasta'

if __name__ == '__main__':
    # filenames_list = list of entered arguments from command line.
    file_in = sys.argv[:1]

#Open output file and write
with open(file_out, 'w') as f_out:
    #as file_in is a list, could have more than one file so we need to iterate.
    for filename in file_in:
        #my_sequence_recorded_iterable is a list, each sequence of the file will have a sequence record,
        #the record is composed by seq, id, name and description.
        my_sequence_recorded_iterable = list(SeqIO.parse(open(filename, mode='r'), 'fasta'))
        # if the length of the list is empty print a warning and write to stderr.
        if len(my_sequence_recorded_iterable) == 0:
            print(f'WARNING file: {filename}: Empty file', file=sys.stderr)
        #now we will iterate on my_sequence_recorded_iterable list, with seq_record elements
        for seq_record in my_sequence_recorded_iterable:
            #seq_record.description=' '.join(seq_record.description.split()[1:])  in here I edit the description
            # as it originally contains the id.
            # we now write each iterated sequence 'seq_record' in our output file f_out as fasta format.
            SeqIO.write(seq_record, f_out, 'fasta')
            #We now print to stdoout.
            print('>' + seq_record.id)
            print(translate(seq_record.seq))





