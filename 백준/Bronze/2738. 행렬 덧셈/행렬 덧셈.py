n,m = map(int,input().split())
lst_a = []
lst_b = []
for _ in range(n):
    lst_a.append(list(map(int, input().split())))
for _ in range(n):
    lst_b.append(list(map(int, input().split())))
    
ans = []
for i in range(n):
    ans.append(lst_a[i])
    for j in range(m):
        ans[i][j] += lst_b[i][j]
        
        
for k in ans:
    print(' '.join(map(str,k)))