from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    map = [[0] * 102 for _ in range(102)] 
    visited = [[False] * 102 for _ in range(102)]

    for a, b, c, d in rectangle:
        for i in range(a * 2, c * 2 + 1):
            for j in range(b * 2, d * 2 + 1):
                if i == a * 2 or i == c * 2 or j == b * 2 or j == d * 2:
                    if map[i][j] == 0:  
                        map[i][j] = 1
                else:
                    map[i][j] = 2 

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    q = deque([[characterX * 2, characterY * 2, 0]])  
    visited[characterX * 2][characterY * 2] = True

    while q:
        x, y, cnt = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            return cnt // 2  
        for i in range(4):
            nx, ny = x + di[i], y + dj[i]
            if 0 <= nx < 102 and 0 <= ny < 102 and not visited[nx][ny] and map[nx][ny] == 1:
                q.append([nx, ny, cnt + 1])
                visited[nx][ny] = True

    return 0
