import sys
iuput = sys.stdin.readline
s = input()
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(input().split()))

tmp = lst[0][0]
prefixsums = {chr(i): [0] * (len(s) + 1) for i in range(ord('a'), ord('z') + 1)}

for i in range(len(s)):
    for alpha in prefixsums:
        if s[i] == alpha:
            prefixsums[alpha][i + 1] = prefixsums[alpha][i] + 1
        else:
            prefixsums[alpha][i + 1] = prefixsums[alpha][i]

for j in range(n):
    a, b, c = lst[j]
    l = int(b)
    r = int(c)
    if l == 0:
        print(prefixsums[a][r + 1])
    else:
        print(prefixsums[a][r + 1] - prefixsums[a][l])