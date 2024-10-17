from collections import deque

def solution(board):
    def in_range(i,j,l):
        if 0<=i<len(l) and 0<=j<len(l[0]):
            return True
        return False
        
    answer = 0
    di,dj = [0,0,-1,1], [-1,1,0,0] # 상 하 좌 우
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 'R':
                rx, ry = x,y
            elif board[x][y] == 'G':
                gx,gy = x,y
    q = deque([[(rx,ry),0]])
    visited = set((rx,ry))
    while q:
        tmp = q.popleft()
        i,j = tmp[0]
        cnt = tmp[1]
        if cnt == (len(board)+ len(board[0])):
            print(cnt)
            return -1
        if i == gx and j == gy:
            return cnt
        for didx in range(4):
            ni,nj = tmp[0]
            while in_range(ni,nj,board) and board[ni][nj] != 'D':
                ni,nj = ni + di[didx], nj + dj[didx]
            ni -= di[didx]
            nj -= dj[didx]
            if (ni,nj) not in visited:
                q.append([(ni,nj),cnt + 1])
                visited.add((ni,nj))
            
    return -1