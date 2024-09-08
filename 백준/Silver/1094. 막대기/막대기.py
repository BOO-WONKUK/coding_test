n = int(input())
tmp = 64
ans = 0
while n:
    if tmp <= n:
        n -= tmp
        ans+=1
    tmp //= 2
print(ans)