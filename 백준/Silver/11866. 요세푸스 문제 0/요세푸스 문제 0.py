from collections import deque
n, k = map(int,input().split())
lst = deque([i for i in range(1, n+1)])
ans = [0] * n

print('<',end ='')

for i in range(n):
    for j in range(k-1):
        tmp = lst.popleft()
        lst.append(tmp)
    if i != n-1:
        print(lst.popleft(), end = ', ')
    else:
        print(lst.popleft(), end = '')

print('>')