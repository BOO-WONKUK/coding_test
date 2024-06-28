n = int(input())
dp = [0]*(n+3)
if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()
elif n == 3:
    print(3)
    exit()
dp[0] = 1
dp[1] = 2
dp[2] = 3
for i in range(3,n+3):
    dp[i] = (dp[(i-2)] + dp[(i-1)])%15746
    if i == n:
        print(dp[i-1])
        exit()