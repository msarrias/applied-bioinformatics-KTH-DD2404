import numpy as np
import pandas as pd
import random

lengthDna = int(input("length: "))

bases = ('A', 'C', 'T', 'G')

def random_dna_sequence(lengthDna):
    return ''.join(np.random.choice(list(bases))
               for _ in range(lengthDna))
myrandomsequence = random_dna_sequence(lengthDna)
print(myrandomsequence)

if __name__ == "__main__":
    print(random_dna_sequence(lengthDna))
