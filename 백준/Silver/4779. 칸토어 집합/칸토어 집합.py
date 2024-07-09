lst=[]

def func(i):
    if i==1:
        return'-'
    return func(i//3) +' '*(i//3)+ func(i//3)

while True:
    try:
        n=3**(int(input()))
        lst.append(func(n))
    except EOFError:
        break

for i in lst:
    print(i)