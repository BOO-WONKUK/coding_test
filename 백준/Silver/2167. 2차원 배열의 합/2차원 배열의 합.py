n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().rstrip().split())))

k = int(input())

for _ in range(k):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            result += lst[i][j]
            
    print(result)