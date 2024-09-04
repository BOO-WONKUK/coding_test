n = int(input())
inp = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append([inp[i],i])

lst.sort(key = lambda x : (x[0],x[1]))

for i in range(n):
    lst[i].append(i)
    
lst.sort(key = lambda x : x[1])
for i in range(n):
    print(lst[i][2], end = ' ')