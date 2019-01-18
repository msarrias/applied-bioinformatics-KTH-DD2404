from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
import sys

def format_to_twenty_characters(alignment_def):
    """
    format_to_ten_characters is a function that limits the sequence_name length to 10.
    :param sequence_name: 
    :return: sequence_name limited to 10 characters.
    
    """
    # if the sequence length is greater than 10 take just the first 10 characters and add 4 spaces this to create 
    # more distance on the matrix.
    if len(alignment_def) > 20:
        return alignment_def[:20]
    # if it's less than ten add blank spaces for the remaining, plus 4 more spaces.
    return sequence_name + ' ' * (20 - len(alignment_def))

def hit_match_funct(alignment_hsps):
        if (hit_match in alignment.hit_def) or (hit_match in alignment.hit_def):
            print(
                record.query,
                format_to_twenty_characters(alignment.hit_def),
                round(hsp.bits, 2),
                hsp.expect
                )
        return True, 'no hits'


if __name__ == '__main__':
    E_VALUE_THRESH = 1e-20
    filename = sys.argv[2]
    hit_match = sys.argv[1]
    with open(filename, 'r') as f:
        blast_records_by_name = NCBIXML.parse(f)
        for record in blast_records_by_name:
            for alignment in record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < E_VALUE_THRESH:
                        hit_match_funct(alignment.hsps)




#
# if __name__ == '__main__':
#     E_VALUE_THRESH = 1e-20
#     filename = sys.argv[2]
#     hit_match = sys.argv[1]
#     with open(filename, 'r') as f:
#         blast_records = NCBIXML.parse(f)
#         for record in blast_records:
#             for alignment in record.alignments:
#                 for hsp in alignment.hsps:
#                      if hsp.expect < E_VALUE_THRESH:
#                         if (hit_match in alignment.hit_def) or (hit_match in alignment.hit_id):
#                             print(
#                                 record.query,format_to_twenty_characters(alignment.hit_def),
#                                 round(hsp.bits,2),
#                                 hsp.expect
#                             )
#
#         print('Warning: No hits')