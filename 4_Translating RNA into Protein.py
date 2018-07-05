#!/usr/bin/python
# -*- coding: utf-8 -*- 
__author__ = 'Иван Богданович'

import time

def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения: %f" % (time.time()-t))
        return res
    return tmp

@timer
def answer(s):
    RNA_table = {'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L',\
                 'AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCU':'S','CCU':'P','ACU':'T','GCU':'A',\
                 'UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S','CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P',\
                 'ACG':'T','GCG':'A','UAU':'Y','CAU':'H','AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D',\
                 'UAA':'','CAA':'Q','AAA':'K','GAA':'E','UAG':'','CAG':'Q','AAG':'K','GAG':'E','UGU':'C','CGU':'R', \
                 'AGU':'S','GGU':'G','UGC':'C','CGC':'R','AGC':'S','GGC':'G','UGA':'','CGA':'R','AGA':'R','GGA':'G',\
                 'UGG':'W','CGG':'R','AGG':'R','GGG':'G'}
    codons = []

    while len(s)>=3:
        codon = s[:3]
        s=s[3:]
        codons.append(RNA_table[codon])
    print(''.join(codons))

dataset = 'AUGUUUUCGUCAUAGCUU'
answer(dataset)