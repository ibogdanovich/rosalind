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
    cmutations = 0
    s, t = dataset.read().split('\n')
    for i in range(len(s)):
        if s[i] != t[i]:
            cmutations +=1
    print(cmutations)

dataset = open('dataset.txt', 'r')
answer(dataset)
dataset.close()