import biolib

DNA_collection =  {}
consensus = []
with open('dataset.txt', 'r') as ds:
    for name, seq in biolib.read_fasta(ds):
        DNA_collection[name[1:]] = seq

    A_list = []
    C_list = []
    G_list = []
    T_list = []
    for i in range(len(seq)):
        sums = {'A':0, 'C':0, 'G':0, 'T':0}
        for key in DNA_collection.keys():
            if DNA_collection[key][i] == 'A': sums['A'] += 1
            if DNA_collection[key][i] == 'C': sums['C'] += 1
            if DNA_collection[key][i] == 'G': sums['G'] += 1
            if DNA_collection[key][i] == 'T': sums['T'] += 1
        max_n = 'A'
        for n, s in sums.items():
            if s > sums[max_n]: max_n = n
        consensus.append(max_n)
        A_list.append(str(sums['A']))
        C_list.append(str(sums['C']))
        G_list.append(str(sums['G']))
        T_list.append(str(sums['T']))
print(''.join(consensus))
print("A: %s" % " ".join(A_list))
print("C: %s" % " ".join(C_list))
print("G: %s" % " ".join(G_list))
print("T: %s" % " ".join(T_list))
