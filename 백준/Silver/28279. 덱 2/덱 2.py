from collections import deque
import sys
n = int(sys.stdin.readline())

lst = deque([])

for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == '1':
        lst.appendleft(s[1])
    elif s[0] == '2':
        lst.append(s[1])
    elif s[0] == '3':
        if lst:
            print(lst.popleft())
        else:
            print(-1)
    elif s[0] == '4':
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif s[0] == '5':
        print(len(lst))
    elif s[0] == '6':
        if not lst:
            print(1)
        else:
            print(0)
    elif s[0] == '7':
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif s[0] == '8':
        if lst:
            print(lst[-1])
        else:
            print(-1)
    
    