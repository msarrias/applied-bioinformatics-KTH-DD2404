#!/usr/bin/env python
# coding: utf-8

import sys
import os
import tempfile
import pexpect
import fileinput
import numbers
import urllib.request
from Bio import SeqIO
from Bio import AlignIO


def format_to_ten_characters(sequence_name):
    """
    format_to_ten_characters is a function that limits the sequence_name length to 10.
    :param sequence_name:
    :return: sequence_name limited to 10 characters.
    """
    # if the sequence length is greater than 10 take just the first 10 characters and add 4 spaces this to create
    # more distance on the matrix.
    if len(sequence_name) > 10:
        return sequence_name[len(sequence_name)-10:]
    # if it's less than ten add blank spaces for the remaining, plus 4 more spaces.
    return sequence_name + ' ' * (10 - len(sequence_name))


# Phylip exe path
path='/Users/user/Desktop/MSM/03-Applied_Bioinformatics - KTH/Labs/applied_bioinformatics_DD2404/05-advanced-assignments/01-neighbor-program/phylip-3.695/exe'


if __name__ == '__main__':

    try:
        infile = sys.argv[1]
    except IndexError:
        sys.stderr.write("Error: You have to specify the name of the file.\n")
        sys.stderr.write("\nUsage:\n    bootstrap <filename> <number of boostraps>\n")
        sys.exit()

    try:
        bootstraps_n = sys.argv[2]
    except IndexError:
        sys.stderr.write("Error: You have to specify the number of boostraps.\n")
        sys.stderr.write("\nUsage:\n    bootstrap <filename> <number of boostraps>\n")
        sys.exit()


    if infile[-3:] != '.fa':
        sys.stderr.write("Error: only fasta format accepted.\n")
        sys.stderr.write("\nUsage:\n    bootstrap <filename> <number of boostraps>\n")
        sys.exit()

    bootstraps_n = str(sys.argv[2])
    # Parse sequences
    records = list(SeqIO.parse(infile, "fasta"))

    long_names = {}
    for i, record in enumerate(records):
        long_names[i] = record.id
        record.id = format_to_ten_characters(record.id)

    tmp_file = tempfile.NamedTemporaryFile(mode='w')
    SeqIO.write(records, tmp_file, "phylip")
    tmp_file.seek(0)

    old_dir = os.getcwd()
    os.chdir(path)

    # bootstrap:
    child = pexpect.spawn('rm infile outfile outtree')
    child = pexpect.spawn('./seqboot')
    args_list = [tmp_file.name, "R", bootstraps_n, "Y", "7"]
    for arg in args_list:
        child.sendline(arg)
    child.expect(pexpect.EOF)
    child = pexpect.spawn("mv outfile infile")
    child.close()

    # distance matrix:
    child = pexpect.spawn('./protdist')
    args_list = ["M", "D", bootstraps_n, "Y"]
    for arg in args_list:
        child.sendline(arg)
    child.expect(pexpect.EOF)
    child = pexpect.spawn("mv outfile infile")
    child.close()

    # phylotrees:
    child = pexpect.spawn('./neighbor')
    args_list = ["M", bootstraps_n, "7", "Y"]
    for arg in args_list:
        child.sendline(arg)
    child.expect(pexpect.EOF)
    child = pexpect.spawn("rm outfile infile")
    child.close()

    f = open("outtree")
    for line in f:
        for i in long_names:
            line = line.replace(records[i].id, long_names[i])
        print(line.rstrip()),
    f.close()

    os.chdir(old_dir)




