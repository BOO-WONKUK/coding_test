from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
lst = deque()
for _ in range(n):
    k = list(map(int, input().split()))
    if k[0] == 1:
        lst.append(k[1])
    elif k[0] == 2:
        try:
            print(lst.pop())
        except:
            print(-1)
    elif k[0] == 3:
        print(len(lst))
    elif k[0] == 4:
        if len(lst)==0:
            print(1)
        else:
            print(0)
    elif k[0]==5:
        try:
            print(lst[-1])
        except:
            print(-1)