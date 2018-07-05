def read_fasta(datafile):
    name, seq = None, []
    for line in datafile:
        line = line.rstrip()
        if line.startswith('>'):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:yield (name, ''.join(seq))

def RNA_splice(RNA, introes):
    introne_index = []
    for item in intrones:
        RNA = RNA.replace(item, '')
    return RNA

def protein_pip(RNA):
    RNA_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',\
                 'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',\
                 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',\
                 'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',\
                 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',\
                 'UAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': '', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', \
                 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',\
                 'UGA': '', 'CGA': 'R', 'AGA': 'R',  'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

    RNA = RNA.replace('T', 'U')
    i = 0
    while i < len(RNA)-2:
        print(RNA_table[RNA[i:i+3]], end='')
        i += 3

intrones = []

with open('dataset.txt') as ds:
    for name, seq in read_fasta(ds):
        intrones.append(seq)
RNA_seq = intrones.pop(0)
RNA_spliced = RNA_splice(RNA_seq, intrones)

print(RNA_spliced)

protein_pip(RNA_spliced)