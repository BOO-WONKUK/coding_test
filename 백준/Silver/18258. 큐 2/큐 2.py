import sys
from collections import deque

n = int(sys.stdin.readline().strip())
lst = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    lst.append(s)

q = deque([])
    
for s in lst:
    if 'push' in s:
        s,n = s.split()
    if s == 'push':
        q.append(n)
    elif s == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s == 'size':
        print(len(q))
    elif s == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])