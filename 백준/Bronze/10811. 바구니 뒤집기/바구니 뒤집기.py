n,m = map(int, input().split())
lst = [i for i in range(1,n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    tmp = lst[a-1:b]
    lst[a-1:b] = tmp[::-1]
print(' '.join(map(str, lst)))