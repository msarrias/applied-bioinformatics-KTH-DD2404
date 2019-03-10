## Motif Filter
## Instructions:
Use BioPython to write a program that reads a Fasta file containing protein sequences and writes those sequences that contain a given motif: K-L-[EI]{2-}-K (in Prosite notation). I.e., we want to extract those sequences that contain KL followed by two or more of either E or I, then a K. Output must be written to stdout (the terminal). You may use the module 're' for this.

## Test data
This document contains 62 proteins and 23 of them contains the motif we want.

Use an empty file to ensure this is also handled well.

You must also put together a small testset yourself.

## Requirements
You must use a regular expression for the filtering. You must write your own test file containing one sequence with the motif and one without it! If a sequence contains the motif, the entire sequence should be written out in Fasta format. Sequences not containing the motif should be discarded. Your program must handle all test files gracefully. Note 1:Only those sequences contaning the required motif are echoed to stdout. No change in the sequences' description is made.

Note 2: The above is a tiny example data set with tiny sequences. In the "big" example, we need the full sequences.


> You Python program. Your test case (see requirement 2). How many KLEEK proteins are there in the test data?

23
