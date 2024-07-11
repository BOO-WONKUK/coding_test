import itertools
n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]

com = list(itertools.combinations_with_replacement(lst, m))

for i in com:
    print(' '.join(map(str,i)))