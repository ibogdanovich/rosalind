with open('dataset.txt', 'r') as ds:
    k, m, n = ds.read().split(' ')
    k = float(k)
    m = float(m)
    n = float(n)
    total = float(k+m+n)
    print (1 - (n/total)*((n-1)/(total-1)) - (n/total)*(m/(total-1)) - (m/total)*((m-1)/(total-1)) *0.25)