from collections import deque
map = [[] for _ in range(200)]
visited = [False]*200

def bfs(node):
    q = deque([node])
    visited[node] = True
    
    while q:
        cur = q.popleft()
        for k in map[cur]:
            if not visited[k]:
                visited[k] = True
                q.append(k)

def solution(n, computers):
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                map[i].append(j)
                map[j].append(i)
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer