import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(list(input()))

bchess_cnt = [[0]*(m+1) for _ in range(n+1)]
wchess_cnt = [[0]*(m+1) for _ in range(n+1)]
    
result = float('inf')
for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0:
            if lst[i][j] == 'B':
                bx = 0
                wx = 1
            else:
                lst[i][j] == 'W'
                bx = 1
                wx = 0
                
            bchess_cnt[i][j] = bx + bchess_cnt[i-1][j] + bchess_cnt[i][j-1] - bchess_cnt[i-1][j-1]
            wchess_cnt[i][j] = wx + wchess_cnt[i-1][j] + wchess_cnt[i][j-1] - wchess_cnt[i-1][j-1]
        else:
            if lst[i][j] == 'W':
                bx = 0
                wx = 1
            else:
                lst[i][j] == 'B'
                bx = 1
                wx = 0
                
            bchess_cnt[i][j] = bx + bchess_cnt[i-1][j] + bchess_cnt[i][j-1] - bchess_cnt[i-1][j-1]
            wchess_cnt[i][j] = wx + wchess_cnt[i-1][j] + wchess_cnt[i][j-1] - wchess_cnt[i-1][j-1]

for i in range(n-k+1):
    for j in range(m-k+1):
        bsum = bchess_cnt[i+k-1][j+k-1] - bchess_cnt[i-1][j+k-1] - bchess_cnt[i+k-1][j-1] + bchess_cnt[i-1][j-1]
        wsum = wchess_cnt[i+k-1][j+k-1] - wchess_cnt[i-1][j+k-1] - wchess_cnt[i+k-1][j-1] + wchess_cnt[i-1][j-1]
        result = min(result, bsum, wsum)
        
print(result)
    