from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
R = int(data[2])

graph = defaultdict(list)
index = 3
for _ in range(M):
    u = int(data[index])
    v = int(data[index+1])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

for key in graph:
    graph[key].sort()

def bfs(start):
    visited = [-1] * (N + 1)
    queue = deque([start])
    order = 1
    visited[start] = order
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                order += 1
                visited[neighbor] = order
                queue.append(neighbor)
    return visited

visited = bfs(R)

for i in range(1, N + 1):
    print(visited[i] if visited[i] != -1 else 0)
