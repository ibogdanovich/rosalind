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
    print(s.count('A'),' ',s.count('C'),' ',s.count('G'),' ',s.count('T'))
answer(dataset)