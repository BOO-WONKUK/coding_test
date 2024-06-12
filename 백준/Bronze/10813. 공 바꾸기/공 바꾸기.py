n, m = map(int, input().split())
lst = [i for i in range(1,n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    tmp = lst[b-1]
    lst[b-1] = lst[a-1]
    lst[a-1] = tmp
    
print(" ".join(map(str,lst)))