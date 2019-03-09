#!/usr/bin/env python
# coding: utf-8

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
            # if the line do not starts with > the keyvalue will take the line value and will
            # join all of the next strings until next >.
            if line[0] != '>':
                genome += line
            dna_sequences_by_name_dict[sequence_name] = genome
    # returns the dictionary with all the read sequences of the file.
    return dna_sequences_by_name_dict


filenames = [
    'bacillus_subtilis.fna',
    'chlamydophila_pneumoniae.fna',
    'haemophilus_influenzae.fna',
    'legionella_pneumophila.fna',
    'thermosynechococcus_elongatus.fna'
]


if __name__ == '__main__':
    for filename in filenames:
        try:
            translate_seq = readGenome(filename)
            print(filename)
            for sequence_name, dna_sequence in translate_seq.items():
                #print(sequence_name)
                print(len(dna_sequence))
               # print(dna_sequence[:15])
        except Exception as e:
            print(filename)
            print(e)
