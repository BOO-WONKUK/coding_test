def func(s):
    for i in range(N-s+1): 
        for j in range(M-s+1): 
            if lst[i][j] == lst[i][j+s-1] == lst[i+s-1][j] == lst[i+s-1][j+s-1]:
                return True

    return False


N, M = map(int, input().split())
lst = [list(map(int, list(input()))) for _ in range(N)]

size = min(N,M)

for k in range(size, 0, -1):
    if func(k):
        print(k**2)
        break