import numpy as np
import pandas as pd
import random


def unif_dna_sequence(lengthDna):
    return ''.join(np.random.choice(list(bases))
            for _ in range(lengthDna))

def random_dna_sequence(lengthDna, probability_distribution):
     return ''.join(np.random.choice(list(bases), p=probability_distribution)
            for _ in range(lengthDna))

if __name__ == "__main__":

    bases = ['A', 'C', 'T', 'G']

    lengthDna = int(input("length: "))

    print("1. Uniform Distribution")
    print("2. Set Nucleotides distribution")
    Choice = int(input("Select distribution: "))

    if (Choice == 1):
        print(unif_dna_sequence(lengthDna))

    else:
        A = float(input("A: "))
        C = float(input("C: "))
        T = float(input("T: "))
        G = float(input("G: "))

        while (A + C + T + G != 1):
            print ("Sum should be 1")
            A = float(input("A: "))
            C = float(input("C: "))
            T = float(input("T: "))
            G = float(input("G: "))

        probability_distribution = [A, C, T, G]
        print(random_dna_sequence(lengthDna, probability_distribution))
