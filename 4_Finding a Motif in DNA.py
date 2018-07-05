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
def answer(dataset):
    s, t = dataset.read().split('\n')
    i = 0
    motif_list = []
    while len(s[i:]) >= len(t):
        if s[i:].find(t) > -1:
            motif_list.append(s[i:].find(t)+(i+1))
            i = s[i:].find(t)+(i+1)
        else: i+=1
    print(''.join(motif_list))

dataset = open('dataset.txt', 'r')
answer(dataset)
dataset.close()