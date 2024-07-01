lst = []
for _ in range(9):
    lst.append(list(map(int, input().split())))
    
max_ = 0
x,y = 0,0
for i in range(len(lst)):
    
    tmp = max(max_, max(lst[i]))
    if tmp > max_:
        max_ = tmp
        x = i
        y = lst[i].index(max_)
print(max_)
print(x+1 ,y+1)