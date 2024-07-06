n = int(input())
lst = []
dance = ['ChongChong']
ans = 1
for _ in range(n):
    a,b = list(map(str,input().split()))
    if a in dance and b in dance:
        continue
    elif a in dance:
        dance.append(b)
        ans +=1
    elif b in dance:
        dance. append(a)
        ans +=1 
print(ans)
    
        