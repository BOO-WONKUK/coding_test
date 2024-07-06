import sys
input = sys.stdin.readline

n, m = map(int, input().split())
freq = {}

for _ in range(n):
    a = input().strip()
    if len(a) >= m:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1

lst = sorted(freq.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for item in lst:
    print(item[0])
