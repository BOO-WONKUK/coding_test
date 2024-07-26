def func(a,b):
    for i in range(2, int(b**0.5 + 1)):
        if a%i == 0 and a<b:
            return 1
    if a % b == 0:
        return 2
    else:
        return 3
    

while 1:
    a,b = map(int, input().split())
    
    if a==0 and b==0:
        exit()
    tmp = func(a,b)
    if tmp == 1:
        print('factor')
    elif tmp == 2:
        print('multiple')
    elif tmp == 3:
        print('neither')