n = int(input())
lst = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):

    x,y = map(int,input().split())
    for i in range(x,x + 10):
        for j in range(y,y + 10):
            if i >= 100 or j >= 100:
                break
            lst[i][j] = 1
sum = 0
for row in range(100):
    sum += lst[row].count(1)

print(sum)