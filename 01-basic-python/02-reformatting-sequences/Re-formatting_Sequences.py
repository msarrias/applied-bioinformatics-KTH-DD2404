def reading_sequences (filename):
    """
    reading_sequences reads the lines of the file and returns it as a list of strings 
    without lines starting with markup # and //, also removing the line breaks /n.
    :param filename: name of the file on the wd.
    """
    with open(filename, "r") as file:
        return list(map(str.strip, [row for row in file.readlines() 
                                    if not row.startswith('#') and not row.startswith('//')]))


def slicer(list_of_strings, slice_length):
    """
    slicer breaks down rows.
    :param list_of_strings: list.
    :param slice_length: maximum characters wide per line.
    """
    return [list_of_strings[i:i + slice_length] for i in range(0, len(list_of_strings), slice_length)]



def flatten(list_of_sublists):
    """
    flatten: flattens a list of lists into a list.
    :param list_of_lists: list with sublists.
    """
    return [item
        for sublist in list_of_sublists for item in sublist]


def re_formatting (file_python_object , filename):
    """
    re_formatting: Reformats the sequences from Stockholm files into Fasta format, depending on the extension .
    :param file_python_object: object, result after applying the reading_sequences function.
    :param filename:name of the file on the wd.
    """
    
    #if the extension of the file is .sthlm, return the reformated file.
    if '.sthlm' in filename:
        # Adds the definition line, followed by an unique identifier.
        pre_pfam_indicator_sth = list(map((lambda x: '>' + x), file_python_object))
        # Removes the tab indicator.
        pre_pfam_tab_split_sth = flatten(list(map(lambda x: x.split('\t'), pre_pfam_indicator_sth )))
        # Splits each element of the list after the first word of each element, creating more elements.
        pre_pfam_split_seq_sth = flatten(list(map(lambda x: x.split(' ', 1), pre_pfam_tab_split_sth)))
        # Filter for non-empty spaces.
        pre_pfam_filter_space_sth = list(filter(None, pre_pfam_split_seq_sth))
        # Apply the slice function to break the lines longer than 60 characters.
        pre_pfam_flattened_slice_sth = [flattened_row for row_string in pre_pfam_filter_space_sth 
                                        for flattened_row in slicer(row_string, 60)]
        
        # Add the line breaks for printing and convert into a list.
        pfam_re_formatted_sth_file = list(map((lambda x: x + '\n'), pre_pfam_flattened_slice_sth))
        
        return pfam_re_formatted_sth_file
    
    #if the extension of the file is .txt, return the reformated file.
    if '.txt' in filename:
        # join first to elements of the list.
        pre_pfam_joint_txt = [" ".join(file_python_object[:2])]+file_python_object[2:]
        # Add indicator and convert into a list.
        pre_pfam_indicator_txt = list(map((lambda x: '>' + x), pre_pfam_joint_txt)  )
        # Splits each element of the list after the first word of each element, creating more elements.
        pre_pfam_split_seq_txt = flatten(list(map(lambda x: x.split(' ', 1), pre_pfam_indicator_txt)))
        # Removes blank spaces from each element of the list.
        pre_pfam_strip_seq_txt = list(map(lambda x: x.strip(), pre_pfam_split_seq_txt))
        # Filter for non-empty spaces.
        pre_pfam_filter_space_txt = list(filter(None, pre_pfam_strip_seq_txt))
        # Apply the slice function to break the lines longer than 60 characters.
        pre_pfam_flattened_slice_txt = [flattened_row for row_string in pre_pfam_filter_space_txt 
                                        for flattened_row in slicer(row_string, 60)]
        
        # Add the line breaks for printing and convert into a list.
        pfam_re_formatted_txt_file = list(map((lambda x: x + '\n'), pre_pfam_flattened_slice_txt))
        return pfam_re_formatted_txt_file


filenames = ['PF00041_seed.txt', 'cornercase.sthlm', 'longseqs.sthlm', 'shortseqs.sthlm']

if __name__ == '__main__':

    print(f" available files: {filenames}")
    print('       ')
    print('       ')
    choice = str(input("Which sequence file:  "))

    # Dictionary containing all the raw files as list objects.
    files = {}
    # Dictionary containing all the Fasta formatted files as list objects.
    fasta = {}

    list_formatted_file = reading_sequences(choice)
    list_fasta_formatted_file = re_formatting(list_formatted_file, choice)

    filename_out = choice.split(".")[0]
    fasta_filename = filename_out + '.fa'
    with open(fasta_filename, "w") as new_fasta_file:
        new_fasta_file.writelines(list_fasta_formatted_file)

    # for filename in filenames:
    #     files[filename] = reading_sequences(filename)
    #     fasta[filename] = re_formatting(files[filename],filename)
    #
    #     filename_out = filename.split(".")[0]
    #     fasta_filename = filename_out + '.fa'
    #     with open(fasta_filename, "w") as new_fasta_file:
    #         new_fasta_file.writelines(fasta[filename])

    # choice = choice.split(".")[0]
    # choice = choice + '.fa'

    with open (fasta_filename, 'r') as f:
        print (f.read())
