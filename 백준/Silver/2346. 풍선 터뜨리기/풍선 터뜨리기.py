from collections import deque

n = int(input())
nums = deque(map(int, input().split()))
lst = deque([i for i in range(2,n+1)])

print('1', end = ' ')
tmp = nums[0]
idx = 0
nums.popleft()

for i in range(n-1):
    if tmp < 0:
        for i in range(abs(tmp)):
            a = lst.pop()
            lst.appendleft(a)
            b = nums.pop()
            nums.appendleft(b)
    else:
        for i in range(tmp-1):
            a = lst.popleft()
            lst.append(a)
            b = nums.popleft()
            nums.append(b)
    tmp = nums[0]
    print(lst.popleft(), end = ' ')    
    nums.popleft()
    
