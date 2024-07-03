import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 10001

for _ in range(n):
    x = int(input())
    lst[x] += 1

for i in range(1, 10001):
    for _ in range(lst[i]):
        sys.stdout.write(f'{i}\n')
