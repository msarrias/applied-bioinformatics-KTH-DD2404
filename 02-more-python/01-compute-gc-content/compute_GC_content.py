#!/usr/bin/env python
# coding: utf-8

import sys


def readGenome(filename):
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


def gc_content(dna_sequences_by_name_dict):
    """
    gc_content is a function that computes the percentage of guanine and cytosine present on a sequence.
    :param dna_sequences_by_name_dict: dictionary with sequence name as key and dna_sequence as keyvalue.
    :return: float rounded on three decimals representing the percentage of G and C on the dna_sequence.
    """
    # for key = sequence_name and keyvalue= dna_sequence as items of the dictionary dna_sequences_by_name_dict:
    for sequence_name, dna_sequence in dna_sequences_by_name_dict.items():
        GC_content_computation = float((dna_sequence.count('G') + dna_sequence.count('C'))) / len(dna_sequence)
        print(round(float(GC_content_computation), 3))


if __name__ == '__main__':
    # list with arguments entered from the command line.
    filenames = sys.argv[1:]
    for filename in filenames:
        translate_seq = readGenome(filename)
        gc_content(translate_seq)