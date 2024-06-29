n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(str, input().split())))
    
lst.sort(key = lambda x :int(x[0]))
for i, j in lst:
    print(i,j)