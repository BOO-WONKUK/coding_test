from collections import deque
n = int(input())
lst = []
for _ in range(n):
    s = input()
    lst.append(s)

q = deque([])
    
for s in lst:
    if 'push' in s:
        s,n = s.split()
    if s == 'push':
        q.append(n)
    elif s == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif s == 'size':
        print(len(q))
    elif s == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif s == 'front':
        if len(q) == 0 :
            print(-1)
        else:
            print(q[0])
    elif s == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])