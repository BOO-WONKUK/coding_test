import sys

m = int(sys.stdin.readline().strip())
S = set()

for _ in range(m):
    lst = sys.stdin.readline().strip().split()
    if len(lst) == 1:
        if lst[0] == "all":
            S = set(list(range(1, 21)))
        else:
            S = set()
    
    else:
        i, num = lst[0], lst[1]
        num = int(num)
        
        if i == "add":
            S.add(num)
        elif i == "remove":
            S.discard(num)
        elif i == "check":
            print(1 if num in S else 0)
        elif i == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)