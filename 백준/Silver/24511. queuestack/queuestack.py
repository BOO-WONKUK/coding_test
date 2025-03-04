from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
lst_a = deque(list(map(int, input().split())))
lst_b = deque(list(map(int, input().split())))
m = int(input())
lst_m = deque(list(map(int, input().split())))

ans = deque([])

for i in range(n-1,-1,-1):
    if lst_a[i] == 0:
        ans.append(lst_b[i])
for i in range(m):
    ans.append(lst_m[i])
    print(ans.popleft(), end = ' ')
            
        