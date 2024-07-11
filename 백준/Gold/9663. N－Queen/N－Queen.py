n = int(input())

def dfs(queen_lst,tmp):
    global ans
    if tmp == n:
        ans += 1
        return 0
    
    for i in range(n):
        can = 1
        for x,y in queen_lst:
            if abs(tmp-x) == abs(i-y) or tmp == x or i == y:
                can = 0
        if can:
            queen_lst.append([tmp,i])
            dfs(queen_lst,tmp+1)
            queen_lst.pop()
result = 0                
for q in range(round(n/2+0.3)):
    ans = 0
    queen_lst = [[0,q]]
    dfs(queen_lst,1)
    if n % 2 == 0:
        result += (ans*2)
    else:
        if q == round(n/2+0.3)-1:
            result += ans
        else:
            result += (ans*2)
print(result)