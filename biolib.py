import re

RNA_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',\
             'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',\
             'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',\
             'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',\
             'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',\
             'UAA': '',  'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': '',  'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', \
             'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',\
             'UGA': '',  'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

start_codon = 'AUG'
stop_codon = ['UAG', 'UGA', 'UAA']

def read_fasta(datafile):
    """
    :param datafile: dataset file in FASTA format
    :return: generator <name>,<sequence>
    Function read FASTA format file and return generator (<name> and <sequence>).
    example:
            with open('dataset.txt') as ds:
                for name, seq in read_fasta(ds):
                    print(name, seq)
    """
    name, seq = None, []
    for line in datafile:
        line = line.rstrip()
        if line.startswith('>'):
            if name: yield (name[1:], ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:yield (name[1:], ''.join(seq))

def read_fasta_stream(fasta_stream):
    fasta = fasta_stream.split('\n')
    name, seq = None, []
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:yield (name, ''.join(seq))


def check_motif(motif, dataset):
    """
    :param motif: that we want to check for entrance in dataset
    :param dataset: list of sequences
    :return: if <motif> is present in all <sequences> return True, else False
    """
    flag = 0
    for item in dataset:
        if motif in item:
            flag += 1
    if flag == len(dataset):
        return True
    return False


def get_triplets(seq):
    i = 0
    while i < len(seq):
        triplet = seq[i:i+3]
        if len(triplet)<3:
            break
        else:
            i +=3
            yield triplet

def reverse_complement(seq):
    """
    :param seq: nucleotids sequence
    :return: The reverse complement of a DNA string is formed by reversing the string and taking the complement of each symbol.
    """
    complement = []
    for i in seq[::-1]:
        if i == 'A':
            complement.append('T')
        elif i == 'C':
            complement.append('G')
        elif i == 'G':
            complement.append('C')
        elif i == 'T':
            complement.append('A')
    return ''.join(complement)


def find_frames(seq):
    """
    :param seq: nucleotids sequence
    :return: list of posible open reading frames (ORF)
    """
    frame_list=[]
    pattern = re.compile(start_codon)
    seq = seq.replace('T', 'U')
    for start in pattern.finditer(seq):
        seq_frame = []
        for triplet in get_triplets(seq[start.start():]):
            if triplet in stop_codon:
                frame_list.append(''.join(seq_frame))
                break
            else:
                seq_frame.append(RNA_table[triplet])
    return frame_list


def into_protein(seq):
    """
    :param seq: nucleotids sequence
    :return: string sequence of proteins
    """
    protein_seq = []
    if seq.find("U") >= 0:
        pass # reading seq by 3 chars, comparing with dict and writing into protein_seq
    else:
        seq.replace('T', 'U') # reading seq by 3 chars, comparing with dict and writing into protein_seq
    return ''.join(protein_seq)