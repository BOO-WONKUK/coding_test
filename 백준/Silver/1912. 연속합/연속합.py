n = int(input())
lst = list(map(int, input().split()))

dp = [0]*n
for i in range(n):
    if i==0:
        dp[i] = lst[0]
    dp[i] = max(lst[i],dp[i-1]+lst[i])
        
print(max(dp))