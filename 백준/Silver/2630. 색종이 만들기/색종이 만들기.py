n=int(input())
lst=[]
blue=0
white=0

for i in range(n):
    a=list(map(int,input().split()))
    lst.append(a)

def func(x,y,n):
    global blue, white
    tmp=lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if lst[i][j]!=tmp:
                func(x,y,n//2)
                func(x+n//2,y,n//2)
                func(x,y+n//2,n//2)
                func(x+n//2,y+n//2,n//2)
                return
    if tmp==1:
        blue+=1
    else:
        white+=1
    return blue, white

func(0,0,n)
print(white)
print(blue)