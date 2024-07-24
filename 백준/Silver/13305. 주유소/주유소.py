from sys import stdin

n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
result = 0

c = cost[0]
for i in range(n - 1):
    if c > cost[i]:
        c = cost[i]
    result += c * lst[i]

print(result)