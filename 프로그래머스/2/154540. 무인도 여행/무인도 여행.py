from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = []

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        total_food = int(maps[r][c])

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    total_food += int(maps[nx][ny])
                    queue.append((nx, ny))
        
        return total_food

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != 'X' and not visited[i][j]:
                days = bfs(i, j)
                islands.append(days)

    return sorted(islands) if islands else [-1]
