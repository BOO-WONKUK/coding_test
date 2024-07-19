from collections import deque

n,m = map(int,input().split())
lst = deque([i for i in range(1,n+1)])
index = list(map(int,input().split()))

count = 0
for num in index:
    while 1:
        if lst[0] == num:
            lst.popleft()
            break
        else:
            if lst.index(num) <= len(lst)//2:
                lst.rotate(-1)
                count += 1
            else:
                lst.rotate(1)
                count += 1

print(count)