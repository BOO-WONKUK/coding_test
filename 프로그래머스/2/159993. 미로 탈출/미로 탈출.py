from collections import deque

def solution(maps):
    def in_range(i,j):
        if 0<=i<len(maps) and 0<=j<len(maps[0]):
            return True
        return False
    
    answer = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                si,sj = i,j
            elif maps[i][j] == 'E':
                ei,ej = i,j
            elif maps[i][j] == 'L':
                li,lj = i,j
                
    q = deque([(si,sj,0)])
    visited = set((si,sj))
    
    di,dj = [0,0,-1,1],[-1,1,0,0]
    tmp = -1
    while q:
        i,j,t = q.popleft()
        if i == li and j == lj:
            si, sj = i,j
            tmp = 1
            break
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            
            if in_range(ni,nj) and maps[ni][nj] != 'X' and (ni,nj) not in visited:
                q.append((ni,nj,t+1))
                visited.add((ni,nj))
                
    if tmp == 1:
        q = deque([(si,sj,t)])
        visited = set((si,sj))
        while q:
            i,j,t = q.popleft()
            if i == ei and j == ej:
                return t
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if in_range(ni,nj) and maps[ni][nj] != 'X' and (ni,nj) not in visited:
                    q.append((ni,nj,t+1))
                    visited.add((ni,nj))
            
    return -1