import itertools

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)


with open('dataset.txt', 'r') as ds:
    n = int(ds.read())
    print(factorial(n))
abc = [str (i) for i in range(1,n+1) ]
for _ in itertools.permutations(abc, n):
    print(' '.join(_))