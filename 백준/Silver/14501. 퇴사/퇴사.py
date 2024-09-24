n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n):
    t, p = lst[i]
    
    if i + 1 <= n:
        dp[i + 1] = max(dp[i + 1], dp[i])
    
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)

print(max(dp))