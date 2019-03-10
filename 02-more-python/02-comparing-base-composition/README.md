## Comparing base composition
## Programming: Composition-based distances

Computing phylogenies for species based on whole genomes is hard for several reasons. Do you work with genes only? How do you then pick the genes? You cannot, in general, align whole genomes because of recombination events that cause large scale differences.

One solution that has been tried is comparing the difference in nucleotide composition. Let πX be the nucleotide composition vector for species X. If all nucleotides have the same frequence in X (which would be surprising), then πX=(0.25, 0.25, 0.25, 0.25).

If genome Y we are looking at is GC rich, then the composition vector might be πY = (0.2, 0.3, 0.3, 0.2), assuming that the nucleotide frequencies are in the order A, C, G, and T.

## Measuring difference in composition
To be able to use composition for distances, we want to have a measure for the difference. In this assignment, we use the root-mean-square distance:

Take the elementwise differences. Square the differences and add them up. Divide the sum by 4 and take the square root. diff(πX,πY) = √ (0.25 * ((0.25-0.2)2 + (0.25-0.3)2 + (0.25-0.3)2 + (0.25-0.2)2))

## Assignment
Write a Python program that takes as input a number of filenames, each pointing to files containing one genomic sequence in Fasta format, and output a distance matrix using the composition difference above.

Suggested solution structure Define a function dist that takes two composition vectors as arguments and returns a difference.
