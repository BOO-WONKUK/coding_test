n = int(input())
lst = list(map(int,input().split()))
lst.sort()
if len(lst) % 2 == 0:
    print(lst[0]*lst[-1])
elif len(lst) == 1:
    print(lst[0]**2)
else:
    print(lst[len(lst)//2]**2)