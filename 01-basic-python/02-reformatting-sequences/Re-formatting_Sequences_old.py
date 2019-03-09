#!/usr/bin/env python
# coding: utf-8

# In[1]:


def slicer(string, slice_length):
    return [string[i:i + slice_length]
            for i in range(0, len(string), slice_length)]

#split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]


# In[2]:


def flatten(string):
    return [item
        for sublist in string for item in sublist]

#flatten = lambda l: [item for sublist in l for item in sublist]


# In[3]:


def reading_sequences (filename):
    with open(filename, "r") as file:
        return list(map(str.strip, [row for row in file.readlines() if not row.startswith('#') and not row.startswith('//')]))
    
    


# In[4]:


def pfam_re_formatting (formated_file_python_object , filename):
    
    if '.sthlm' in filename:
        pre_pfam_indicator_sth = list(map(( lambda x: '>' + x), formated_file_python_object))
        pre_pfam_tab_split_sth = flatten(list(map(lambda x: x.split('\t') , pre_pfam_indicator_sth )))
        pre_pfam_split_seq_sth = flatten(list(map(lambda x: x.split(' ', 1) , pre_pfam_tab_split_sth)))
        pre_pfam_filter_space_sth = list(filter(None, pre_pfam_split_seq_sth))
        pre_pfam_flattened_slice_sth = [flattened_row for row_string in pre_pfam_filter_space_sth
                                        for flattened_row in slicer(row_string, 60)]
        pfam_re_formatted_sth_file = list(map(( lambda x: x + '\n'), pre_pfam_flattened_slice_sth))
        
        return pfam_re_formatted_sth_file
        
    if '.txt' in filename:
        pre_pfam_joint_txt = [" ".join(formated_file_python_object[:2])]+formated_file_python_object[2:]
        pre_pfam_indicator_txt = list(map(( lambda x: '>' + x), pre_pfam_joint_txt)  )
        pre_pfam_split_seq_txt = flatten(list(map(lambda x: x.split(' ', 1) , pre_pfam_indicator_txt)))
        pre_pfam_strip_seq_txt = list(map(lambda x: x.strip(), pre_pfam_split_seq_txt))
        pre_pfam_filter_space_txt = list(filter(None, pre_pfam_strip_seq_txt))
        pre_pfam_flattened_slice_txt = [flattened_row for row_string in pre_pfam_filter_space_txt for flattened_row in slicer(row_string, 60)]
        pfam_re_formatted_txt_file = list(map(( lambda x: x + '\n'), pre_pfam_flattened_slice_txt))
        return pfam_re_formatted_txt_file
    


# In[5]:


filenames = ['shortseqs.sthlm','longseqs.sthlm','cornercase.sthlm','PF00041_seed.txt']

files = {}
Fasta = {}

if __name__ == "__main__":
    for filename in filenames:
        files[filename] = reading_sequences(filename)
        
    for filename in filenames:
        Fasta[filename] = pfam_re_formatting(files[filename],filename)
        Fasta_filename = 'Fasta_' + filename
        with open(Fasta_filename, "w") as new_fasta_file:
            new_fasta_file.writelines(Fasta[filename])        
        
        


# In[18]:


get_ipython().system('cat shortseqs.sthlm')


# In[6]:


print(filenames)
print('       ')
print('       ')
Choice = str(input("Which sequence file: "))


# In[11]:


if Choice == 'shortseqs.sthlm':
    with open('Fasta_shortseqs.sthlm', 'r') as f:
           print f.read()
    f.close()
                
if Choice == 'longseqs.sthlm':
    with open('Fasta_longseqs.sthlm', 'r') as ls:
           print ls.read()
    ls.close()
                

if Choice == 'cornercase.sthlm':
    with open('Fasta_cornercase.sthlm', 'r') as cc:
           print cc.read()
    cc.close()
                
if Choice == 'PF00041_seed.txt':
    with open('Fasta_PF00041_seed.txt', 'r') as pf:
           print pf.read()
    pf.close()
else:
    pass
    


# In[ ]:




