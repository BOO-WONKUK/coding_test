lst = list(map(int, input().split()))
lst.sort()
if lst.count(max(lst)) == 3:
    print(sum(lst))
else:
    if lst[0] + lst[1] <= lst[2]:
        if lst[0] == lst[1] == lst[2]:
            print(lst[0]*3)
        else:
            print((lst[0] + lst[1])*2 - 1)
    else:
        print(sum(lst))