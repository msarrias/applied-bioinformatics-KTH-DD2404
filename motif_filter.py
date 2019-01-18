import sys
import re
import urllib.request
from Bio.Seq import Seq, transcribe, translate
from Bio import SeqIO

def checking_for_errors_in_filename(filenames_list):
    """
    checking_for_errors_in_filename is a function that evaluates two scenarios in which the file reading could go wrong.
    :param filenames_list: is a list containing filenames passed as arguments from the command line.
    :return: Boolean and an error message, TRUE if there's an error with the file and FALSE otherwise.
    """

    for filename in filenames_list:
        try:
            #if the files opens correctly pass.
            with open(filename, 'r') as my_file:
                pass
        # if it doesn't pass the exception as e
        except Exception as e:
            # return TRUE and e
            return True, e
        # if the filename extension is not 'fa' raise an error message.
        if filename[-3:] != '.fa':
            # return TRUE, error message
            return True, 'only fasta format accepted'

    return False, ''

if __name__ == '__main__':

    # filenames_list = list of entered arguments from command line.
    file_in = sys.argv[1]
    f_out = 'motif_sequence.fa'
    # has_errors, error_message = checking_for_errors_in_filename(file_in)
    # # if has_errors is TRUE
    # if has_errors:
    #     # print the error message and write it on stderr.
    #     print(error_message, file=sys.stderr)
    #     # raise Exception and stop the programs execution, message: 'wrong entry'.
    #     raise Exception('wrong entry')

    # Prosite notation: K-L-[EI]{2-}-K
    pattern = re.compile("KL[EI]{2,}K")
    my_sequence_recorded = list(SeqIO.parse(open(file_in, mode='r'), 'fasta'))
    # print(len(my_sequence_recorded_iterable))

    my_sequence_recorded_motif = []
    for seq in my_sequence_recorded:
        for match in re.finditer(pattern, str(seq.seq)):
            my_sequence_recorded_motif += [seq]
            print('>' + seq.id)
            print(seq.seq)
    print(len(my_sequence_recorded_motif))
    SeqIO.write(my_sequence_recorded_motif, f_out, 'fasta')