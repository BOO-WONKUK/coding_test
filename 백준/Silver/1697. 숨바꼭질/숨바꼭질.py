from collections import deque

def bfs():
    q = deque()  
    q.append(n)          
    while  q:
        x = q.popleft()  
        if x == k:
            print(lst[x])
            break
        for i in (x - 1, x + 1, x * 2):   
            if 0 <= i <= max_ and not lst[i]:
                lst[i] = lst[x] + 1
                q.append(i)  

max_ = 10 ** 5   
lst = [0] * (max_ + 1) 
n, k = map(int, input().split())

bfs()