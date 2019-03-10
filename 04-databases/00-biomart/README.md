> ## Biomart:
is a system that enables a uniform programmatic interface to many different online databases, and one of the features is that it also offers a web based interface for creating and executing queries and convenient access to large sets of resulting data.

> ## Gene, transcripts, and proteins:
Each gene tells the cell how to put together the building blocks for one specific protein. However, the gene (DNA) sits inside a different compartment of the cell (the nucleus) from the location of the cellular machines that make proteins (ribosomes). Therefore, the gene must first make a copy of itself (called messenger RNA - mRNA), which is smaller and more portable than DNA and is able to leave the nucleus to reach the ribosomes. A ribosome then reads each set of three nucleotides in the mRNA code and converts the instructions into a chain of amino acids that attach together to form a protein. The mRNA also tells the ribosome where to start the protein and when the protein is finished; namely, when it should stop attaching new amino acids to the protein. Because the nucleotides are read in groups of three, it is important for the ribosome to know how to group the nucleotides. If the nucleotides are grouped incorrectly, the ribosome will choose the wrong amino acids and the protein will not function. Usually, when a protein is not properly produced, it is because there is some mutation in the gene which contains its instructions
A primary transcript is the single-stranded ribonucleic acid (RNA) product synthesized by transcription of DNA, and processed to yield various mature RNA products such as mRNAs, tRNAs, and rRNAs.
Exons and introns:
exons and introns are features of DNA, whereas codons are features of RNA. Homologous sequences in the other type of nucleic need to be called something else, otherwise there is a danger the roles of DNA and RNA in the Central Dogma ("DNA makes RNA makes Protein") will be confused. \ Introns or the intervening sequence are considered as the non-coding part of the genes, while the exons or the expressed sequence are known to be as the coding part for proteins of the genes. Introns are the common attribute found in the genes of the multicellular eukaryotes like humans, while exons are found in both prokaryotes and eukaryotes.

> ## Introns:
The transcribed part of the nucleotide sequence in mRNA, which is known to carry the non-coding part for the proteins.
In eukaryotes only.
Non-coding DNA.
These bases are situated between two exons.
Introns remain in the nucleus, even after the mRNA splicing.
These are the less conserved sequence.
They are present in DNA as well as in mRNA primary transcript.

> ## Exons:
The transcribed part of the nucleotide sequence in mRNA, responsible for the protein synthesis.
In both prokaryotes and in eukaryotes.
Coding DNA.
These are the bases which are mainly known for coding the amino acid sequence for the protein.
Exons move to the cytoplasm from the nucleus, when mature mRNA is produced.
These are the highly conserved sequence.
They mark their presence in DNA as well as in mature mRNA.

> ## Untranslated regions (UTR):
The mRNA is initially transcribed from the corresponding DNA sequence and then translated into protein. However, several regions of the mRNA are usually not translated into protein, including the 5' and 3' UTRs.

3' UTR Transcript The region of a coding cDNA downstream of the stop codon which is not translated.
5' UTR Transcript The region of a coding cDNA upstream of the start codon which is not translated.
## Alternative transcripts: Alternative slicing/processing?
Same mRNA transcript can be sliced in different ways. The same initial transcript can yield different mRNAs and therefore different proteins, this is buil with our exons and taking out the introns. maybe in different areas in the body the mRNA is sliced differently, and they have different poly-A sites.

## Homolog, ortholog, paralog:
Homologous genes found in different species that evolved from a common ancestor are called. The term "homolog" may apply to the relationship between genes separated by speciation (ortholog), OR to the relationship between genes originating via genetic duplication (see paralog).

> ## Paralogs: 
genes that are coding diff proteins but are present in the same species.
> ## Orthologs:
Orthologs are genes in different species that have evolved from a common ancestral gene via speciation. present in different species and are exactly the same.
> ## Homologs: 
combination of orthologs and paralogs genes.

## Trying Ensembl BioMart
> Go to Ensembl's BioMart . and choose the "Ensembl Genes 90" database (or later if they have updated the database after this writing). Then choose the Homo sapiens dataset.

> Try the "count" button. Ensembl should respond by claiming it has 63,967 genes for human (as of 2017-11-24). You get this many genes because Ensembl has included RNA genes and pseudogenes. = 

64914.

> How many unique protein-coding genes are there then? Use filters to list those genes that have the type "protein coding". = 22687/64914.
How many of the protein coding genes have been assigned an ID by the Human Gene Nomenclature Committee (HGNC)? (There should be fewer than in the previous question.)

22686
> How many genes have an orthologue in mouse? Use the homologue filter. 

27987

## Retrieving results

The page you get when you click "Results" is just a sample of the full list of resulting data.

> In what basic formats can you download your results? 
HTML CSV TSV

Figure out and explain what the top buttons, labeled "URL", "XML", and "Perl", are for. URL: extension of my personalized query. XML: filters applied Perl API.
Downloadning sequences
Restrict your gene set to contain only those genes coding for proteins containing a domain with the Pfam  identifier PF00104. This should give you 53 genes.

> What sequence format is used for downloading sequences? 
FASTA

> In the "attributes" settings, you can choose what kind of sequences you download. What is the difference between "unspliced transcript" and "unspliced gene"? 


A gene is a set of alternatively spliced Transcripts.The physical genomic location of a number of francripts. A Transcript is a set of exons, introns are not explicitly defined in the database. We can have several Transcripts on different locations of a gene, we only store the exons. We can see it as a herarchy. Translations are not Feauturs, A translation object defines the UTR and CDS of a Transcript. Peptids are not stored in the database, they are computed on the fly using Transcript objects. Not all transcripts have a translation. ncRNAs (non coding RNA)

> Unspliced gene: 

gensequence

> unspliced transcript: 

pre - mRNA, containing exons and introns, primary transcript. What is the difference between "unspliced transcript" and "cDNA"?
cDNA library, complementary DNA, is a single string of DNA. we use reverse transcription of the mRNA is the cDNA. cDNA Transcript The sequence of the spliced exons of a transcript expressed in DNA notation (T rather than U), representing the coding or sense strand. The cDNA contains the whole sequence of the RNA, including coding and untranslated sequence.

> Suppose you want to work with genes' coding regions. If you download the "coding sequence" for your 53 genes, how many sequences do you get? Explain the discrepancy.

CDS Transcript CoDing Sequence. The region of a cDNA which is translated. In Ensembl displays, the stop codon is included as part of the CDS sequence.
