n, m = map(int, input().split())  
lst = list(map(int, input().split())) 

for i in range(m):
    lst.sort()

    x = lst[0] + lst[1]
    lst[0] = x
    lst[1] = x

print(sum(lst))