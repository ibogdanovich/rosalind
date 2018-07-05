import biolib


abc = ['A', 'C', 'G', 'T']
with open('../dataset.txt', 'r') as ds:
    seq = ds.read().strip()
    for _ in abc:
        print(seq.count(_), end=' ')