n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [0,0,0]
for i in range(len(lst)):
    a = dp[0]
    b = dp[1]
    c = dp[2]
    if i ==  0:
        dp[0] = lst[0][0]
        dp[1] = lst[0][1]
        dp[2] = lst[0][2]
    else:
        dp[0] = min(b + lst[i][0], c + lst[i][0])
        dp[1] = min(a + lst[i][1], c + lst[i][1])
        dp[2] = min(b + lst[i][2], a + lst[i][2])

print(min(dp))