def frab(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return frab(n-1, k)+k*frab(n-2, k)

with open('dataset.txt') as ds:
    n, k = ds.readline().split()
    print(frab(int(n), int(k)))