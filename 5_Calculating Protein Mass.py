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
    mass_table = {'A': '71.03711','C': '103.00919','D': '115.02694','E': '129.04259','F': '147.06841','G': '57.02146','H': '137.05891','I': '113.08406','K': '128.09496','L': '113.08406','M': '131.04049','N': '114.04293','P': '97.05276','Q': '128.05858','R': '156.10111','S': '87.03203','T': '101.04768','V': '99.06841','W': '186.07931','Y': '163.06333'}
    s = dataset.read()
    mass = 0
    for i in range(len(s)):
        mass += float(mass_table[s[i]])
    print("%.3f" % mass)

dataset = open('dataset.txt', 'r')
answer(dataset)
dataset.close()