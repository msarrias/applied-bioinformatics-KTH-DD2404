
## Translate DNA

### Instructions:
Write a program that finds the longest open reading frame (ORF) , although not necessarily with a start codon. I.e., you are to find the longest sequence of codons without a stop codon in each input DNA sequence. The output is the ORFs translated to proteins using the genetic code. The output should be formatted as in the previous assignment (Länkar till en externa sida.)Länkar till en externa sida.!

### To present:
What are the "stop codons" in the standard code? Why are we talking about a "standard code"? Looking for the longest ORF is a primitive way to find genes in prokaryotic genomes. Why does it not work for eukaryotes?

### Your code.
How did you structure your code and why? Test runs showing that requirements are fulfilled. What is the longest protein snippet produced on the file an_exon.fa? Why should a real ORF finder also look at the so-called Watson-Crick complement?

### Requirements
Input is one or more sequences in Fasta format. The longest ORF in each sequence should be translated. It may start from any codon. Only the positive strand needs to be considered (i.e., reading left-to-right). Your program must gracefully handle ambigous characters. Translate to X if it is not a regular codon. Your program must be well structured and be written with functions performing important algorithmic steps.
