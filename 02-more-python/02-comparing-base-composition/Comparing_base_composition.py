# !/usr/bin/env python
# coding: utf-8

import urllib.request
import math
import numpy
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
            # if the line do not starts with > the keyvalue will take the line value and will join all of the
            # next strings until next >.
            if line[0] != '>':
                genome += line
            dna_sequences_by_name_dict[sequence_name] = genome
    # returns the dictionary with all the read sequences of the file.
    if len(dna_sequences_by_name_dict) != 1:
        print(f'file: {filename} contains zero or more than one dna sequence', file=sys.stderr)
        raise Exception('wrong file content')
    if len(dna_sequences_by_name_dict[sequence_name]) == 0:
        print(f'file: {filename} empty dna sequence', file=sys.stderr)
        raise Exception('empty dna sequence')
    return dna_sequences_by_name_dict


def composition_vector(dna_sequence):
    """
    composition_vector is a function that weights the nucleotides (A,C,G,T) frequencies on the dna_sequence.
    :param dna_sequence: DNA sequence
    :return: vector with three elements as percentages of the composition weight (A,C,G,T).
    """
    content_A = dna_sequence.count('A')
    content_C = dna_sequence.count('C')
    content_G = dna_sequence.count('G')
    content_T = dna_sequence.count('T')
    length = float(content_A + content_C + content_G + content_T)
    length_other_nucleotides = len(dna_sequence) - length

    if length_other_nucleotides != 0:
        percentage_other_nucleotides = round(float(length_other_nucleotides / len(dna_sequence)), 4)

        print(
            f'WARNING: The genome sequence contains {percentage_other_nucleotides * 100} %'
            ' of nucleotides other than A,C,G,T ',
            file=sys.stderr
        )
    return (
        round(float(content_A / length), 4),
        round(float(content_C / length), 4),
        round(float(content_G / length), 4),
        round(float(content_T / length), 4)
    )


def distance(a_comp_vector, b_comp_vector):
    """
    distance is a function that measueres the distance of two vectors, using the root-mean-square distance.
    :param a_comp_vector: compasition vector for a given genome a.
    :param b_comp_vector: compasition vector for a given genome b.
    :return: single value with the two vectors distance.
    """
    d = [
        ((a_comp_vector[0] - b_comp_vector[0]) ** 2), ((a_comp_vector[1] - b_comp_vector[1]) ** 2),
        ((a_comp_vector[2] - b_comp_vector[2]) ** 2)
    ]

    return round(math.sqrt(0.25 * (d[0] + d[1] + d[2])), 4)


def format_to_ten_characters(sequence_name):
    """
    format_to_ten_characters is a function that limits the sequence_name length to 10.
    :param sequence_name:
    :return: sequence_name limited to 10 characters.

    """
    # if the sequence length is greater than 10 take just the first 10 characters and add 4 spaces this to create
    # more distance on the matrix.
    if len(sequence_name) > 10:
        return sequence_name[:10] + '  '
    # if it's less than ten add blank spaces for the remaining, plus 4 more spaces.
    return sequence_name + ' ' * (10 - len(sequence_name)) + '  '


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

def convert_matrix_row(matrix_row):
    """
    matrix_row is a function that edits the matrix rows so no brackets are written on the output file
    :param matrix_row:
    :return:
    """
    matrix_str_row = ''
    for value in matrix_row:
        matrix_str_row += f'{value}'+ ' '
    return matrix_str_row[:-1] + '\n'


if __name__ == '__main__':

    # filenames_list = list of entered arguments from command line.
    filenames_list = sys.argv[1:]
    # we want to check if there is an error message related with the files we are trying to open, we apply the
    #function checking_for_errors_in_filename.
    has_errors, error_message = checking_for_errors_in_filename(filenames_list)
    #if has_errors is TRUE
    if has_errors:
        # print the error message and write it on stderr.
        print(error_message, file=sys.stderr)
        # raise Exception and stop the programs execution, message: 'wrong entry'.
        raise Exception('wrong entry')

    dna_sequence_by_name = dict()
    for filename in filenames_list:
        translate_seq = readGenome(filename)
        #for each element(filename) apply readGenome function which will result in a dictionary with sequence name as key
        # and sequence as value, iterate through all the files names, giving as a result a dictionary containing all the
        #sequences of the files entered from command line.
        dna_sequence_by_name = {**dna_sequence_by_name, **translate_seq}

    # composition_dna_sequence_by_name is a dictionary, key: 10 characters sequence name, and value: matrix vector
    # without brackets. We iterate on the dna_sequence_by_name dictionary.
    composition_dna_sequence_by_name = {
        format_to_ten_characters(sequ_name): composition_vector(dna_sequence)
        for sequ_name, dna_sequence in dna_sequence_by_name.items()
    }
    #create empty matrix
    my_matrix = numpy.zeros((len(composition_dna_sequence_by_name), len(composition_dna_sequence_by_name)))

    # start iterating with index as key and sequence vector as value
    for index, sequence_vector_a in enumerate(composition_dna_sequence_by_name.values()):
        #we start a new for with a new index to compute the distances with the previous index.
        for index_2, sequence_vector_b in enumerate(composition_dna_sequence_by_name.values()):
            # we fill the empty  matrix
            my_matrix[index, index_2] = distance(sequence_vector_a, sequence_vector_b)

    # create the new output file were we will write.
    output_file = open('distance_matrix', 'w')
    print(len(filenames_list))

   #
    distance_matrix_rows_list = ['    '+f'{len(filenames_list)}\n']

    for index, sequence_name in enumerate(composition_dna_sequence_by_name.keys()):
        print(sequence_name, my_matrix[index])
        distance_matrix_rows_list.append(sequence_name + convert_matrix_row(my_matrix[index]))
    output_file.writelines(distance_matrix_rows_list)
    output_file.close()
