from collections import deque

def solution(board):
    def in_range(i, j, l):
        return 0 <= i < len(l) and 0 <= j < len(l[0])
        
    answer = 0
    di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]  # 좌, 우, 상, 하
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 'R':
                rx, ry = x, y
            elif board[x][y] == 'G':
                gx, gy = x, y
                
    q = deque([((rx, ry), 0)])
    visited = set([(rx, ry)])
    
    while q:
        (i, j), cnt = q.popleft()

        # 목표 지점에 도달하면
        if i == gx and j == gy:
            return cnt

        # 상, 하, 좌, 우로 이동
        for didx in range(4):
            ni, nj = i, j
            while in_range(ni, nj, board) and board[ni][nj] != 'D':
                ni, nj = ni + di[didx], nj + dj[didx]
            
            # 이동할 수 없는 곳까지 갔을 때, 한 칸 뒤로
            ni, nj = ni - di[didx], nj - dj[didx]

            # 이미 방문한 좌표가 아니라면 큐에 추가
            if (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append(((ni, nj), cnt + 1))

    return -1
