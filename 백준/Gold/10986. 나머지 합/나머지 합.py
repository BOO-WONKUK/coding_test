n, m = map(int, input().split())
a = list(map(int, input().split()))

r = [0] * m
prefixsum = 0
for i in range(n):
    prefixsum += a[i]
    r[prefixsum % m] += 1

ans = r[0] 
for i in range(m):
    ans += r[i] * (r[i]-1) // 2
print(ans)