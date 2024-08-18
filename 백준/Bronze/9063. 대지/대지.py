N=int(input())
x=[]
y=[]

for _ in range(N):
    a,b=map(int, input().split())
    if(N==1):
        print(0,end='')
        exit(0)
    else:
        x.append(a)
        y.append(b)

print((int(max(x))-int(min(x)))*(int(max(y))-int(min(y))),end='')