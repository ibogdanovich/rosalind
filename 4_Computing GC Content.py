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

def cg_count(seq):
    return (seq.count('C')+seq.count('G'))/len(seq)*100

@timer
def answer(s):
    seq_dict = {}
    seq_list = s.read().split('>')
    final = {}
    for ent in seq_list:
        if len(ent) > 0:
            s = ent.split('\n')
            ident = s.pop(0)
            seq_dict[ident] = ''.join(s).strip()
    for i in seq_dict:
        final[i] = cg_count(seq_dict[i])
    print(final)


datafile = open('dataset.txt', 'r')

dataset = datafile
answer(dataset)
datafile.close()