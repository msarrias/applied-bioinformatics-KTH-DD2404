#!/usr/bin/env python
# coding: utf-8

from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import statistics
import argparse

def main():
    parser = argparse.ArgumentParser(description="Visualise Blast results")

    parser.add_argument("-i", "--input", metavar="INPUT_BLAST_FILE",
                        help="Input file, Blast output file in xml format")
    parser.add_argument("-o", "--output", metavar="OUTPUT_SCORE_HIST",
                        help="Output histogram file in PDF format.")

    args = parser.parse_args()

    filename = args.input
    out_file = args.output

    blast_records_by_name = dict()
    scores = []
    with open(filename, 'r') as f:
        blast_records_name = filename[:-4] + '_br'
        blast_records_by_name[blast_records_name] = NCBIXML.parse(f)
        for record in blast_records_by_name[blast_records_name]:
            for alignment in record.alignments:
                for hsp in alignment.hsps:
                    scores.append(hsp.bits)

    plt.hist(scores, color='#607c8e', bins=10, rwidth=0.9)
    plt.grid(axis='y')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Scores for the first Blast result')
    plt.figtext(1.0, 0.85,  f'nº hits: {len(scores)}')
    plt.figtext(1.0, 0.80, f'min score: {min(scores)}')
    plt.figtext(1.0, 0.75, f'max score: {max(scores)}')
    plt.figtext(1.0, 0.70, f'scores mean: {round(statistics.mean(scores),2)}')
    plt.savefig(out_file)
    plt.show()

if __name__ == "__main__":
    main()







