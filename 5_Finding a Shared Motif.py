# Нужно почистить код и немного оптимизировать

from biolib import read_fasta

def check_motif(motif, dataset):
    flag = 0
    for item in dataset:
        if motif in item:
            flag += 1
    if flag == len(dataset):
        return True
    return False

sequences = []
with open('dataset.txt') as ds:
    for name, seq in read_fasta(ds):
        sequences.append(seq)

base_seq = sequences.pop(0)
max_len = len(base_seq)
motifs = []
for j in range(max_len):
    for i in range(max_len):
        m = base_seq[j:i+1]
        if m:
            motifs.append(m)

common_motifs = []
for motif in motifs:
    if check_motif(motif, sequences):
        common_motifs.append(motif)
common_motifs.sort(key=len)
print(common_motifs[-1])
