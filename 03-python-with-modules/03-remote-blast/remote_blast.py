from Bio.Blast import NCBIWWW
import sys

if __name__ == '__main__':

    file_in = sys.argv[1]

    fasta_string = open(file_in).read()
    result_handle = NCBIWWW.qblast("blastp", "nr", fasta_string)
    print(result_handle.getvalue())

    # with open("my-output1.xml", 'w') as f:
    #     f.write(result_handle.getvalue())
    # print('done! you can now look for your xml file in your directory')