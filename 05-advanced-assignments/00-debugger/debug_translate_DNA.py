#!/usr/bin/env python
# coding: utf-8

import sys
import pdb

# GENCODE dictionary, from DNA nucleotides codons to aminoacids.
##Read it from a file.
GENCODE = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}


def readGenome(filename: object):
    """
    readGenome is a function that opens a Fasta format file available in the wd and reads the sequences on it.
    :param filename: name of the file on the wd.
    :return: a dictionary with genome name as key and the sequence as keyvalue.
    """
    # dna_sequences_by_name_dict is a dictionary with keys: genome name, values: sequence.
    dna_sequences_by_name_dict = dict()
    # Opens the file listed in filenames.
    with open(filename, 'r') as f:
        # for each line on the file:
        for line in f:
            # removes the entry key.
            line = line.strip()
            # if the line starts with > the key value will be empty, while the key will take the value of the line.
            if line[0] == '>':
                genome = ''
                sequence_name = line
            # if the line do not starts with > the keyvalue will take the line value and will join all of the next strings until next >.
            if line[0] != '>':
                genome += line
            dna_sequences_by_name_dict[sequence_name] = genome
    # returns the dictionary with all the read sequences of the file.
    return dna_sequences_by_name_dict


def decode_dna(dna_sequence_):
    """
    decode_dna is a function that translates a DNA sequence into aminoacids, starting from the first, second
    and third position of the sequence.
    :param dna_sequence_: keyvalue of the dna_sequences_by_name_dict dictionary, created on the readGenome function.
    :return: a vector with the translated DNA sequences into proteins, starting from the different positions.
    each sequence will have three different reading frames.
    Example: dna_seq = (ATGGGTTGG); for i in range(0, len(dna_seq),3); print(dna_seq[i]); A G T...
    """

    def compute_protein_translation(dna_sequence):
        """
        compute_protein_translation is a function that translates a DNA sequence into aminoacids.
        :param dna_sequence: keyvalue of the dna_sequences_by_name_dict dictionary, created on the readGenome function.
        :return: a list with the translated sequence, only one element.
        """
        # starts with an empty list
        protein = ''
        # verify if the sequence is multiple of 3
        sequence_length = len(dna_sequence) % 3
        # if it's not:
        if sequence_length != 0:
            # as we start reading the sequence from the first nucleotide we don't take into account
            # the last incomplete triplete.
            dna_sequence = dna_sequence[:-sequence_length]
        # for all the elements of the read dna sequence starting from 0 and counting by each 3 elements.
        for i in range(0, len(dna_sequence), 3):
            # define each codon.
            codon = dna_sequence[i:i + 3]
            # translate and construct the translated protein string. Takes the codon looks into the dictionary
            # and translates, if there's not a match replace with an 'X'.
            protein += GENCODE.get(codon, 'X')
        # returns the translated protein string.
        return protein

    # repeat the same function starting from the first, second and third position.
    decoded_from_first_position = compute_protein_translation(dna_sequence_)
    decoded_from_second_position = compute_protein_translation(dna_sequence_[1:])
    decoded_from_third_position = compute_protein_translation(dna_sequence_[2:])
    # return a vector with the three possible reading frames.
    return [decoded_from_first_position, decoded_from_second_position, decoded_from_third_position]


# List of files available for translate in Fasta format in the wd.
filenames = ['an_exon.fa', 'cornercase.fa', 'longseqs.fa', 'PF00041_seed.fa', 'shortseqs.fa']


def main():
    print(filenames)
    print('       ')
    print('       ')
    filename_seq = input("Which file: ")

    # dictionary with keys: dna_name, values: sequence_name.
    pdb.set_trace()
    translate_seq = readGenome(filename_seq)

    # for key, keyvalue in the dictionary items.
    for sequence_name, dna_sequence in translate_seq.items():
        # decode the dna sequence with the decode_dna function. This will return a vector of three elements.
        decoded_dna_list = decode_dna(dna_sequence)

        # longest_protein_sequence is the longest sequence found until the next stop codon,
        # arg1 : max sequence of each frame after splitting on each stop codon, we iterate for each element of the list.
        # key function = length.
        longest_protein_sequence = max(
            [max(decoded_dna.split('_'), key=len) for decoded_dna in decoded_dna_list],
            key=len
        )
        # print the sequence name.
        print(sequence_name + '\n')
        # print the translated sequence. Which will be a list with three different reading frames.
        print(decoded_dna_list)
        print('\n')
        print(f'The longest sequence has length: {len(longest_protein_sequence)}')
        print(longest_protein_sequence)


if __name__ == '__main__':
    main()
