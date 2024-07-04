n,r = map(int, input().split())
u = 1
d = 1

for i in range(n-r+1,n+1):
    u *= i
for j in range(1,r+1):
    d *= j
print(u//d)