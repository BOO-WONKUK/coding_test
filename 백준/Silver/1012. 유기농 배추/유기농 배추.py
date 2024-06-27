from collections import deque

t = int(input())


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(lst, x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n :
                if lst[nx][ny] == 1:
                    lst[nx][ny] = 0
                    q.append((nx,ny))

for _ in range(t):
    m,n,k = map(int, input().split())
    lst = [[0]*n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        a,b = map(int, input().split())
        lst[a][b] = 1
    
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1:
                dfs(lst, i, j)
                cnt += 1
    print(cnt)