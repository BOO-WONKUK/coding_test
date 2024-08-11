N = int(input())
d = list(map(int, input().split()))
s = N * N * 5
a = 0

if N == 1:
    d.sort()
    print(sum(d[:5]))
else:
    a = 0
    p = []
    for i in range(3):
        p.append(min(d[i], d[-1-i]))
    p.sort()
    a += 4 * sum(p)
    s -= 4 * 3
    a += (8 * N - 12) * sum(p[:2])
    s -= (8 * N - 12) * 2
    a += s * p[0]
    print(a)
