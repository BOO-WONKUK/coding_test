import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
result= [-1]*n
stack = [0] 

for i in range(1, n):
    while stack and lst[stack[-1]] < lst[i]:
        result[stack.pop()] = lst[i] 
    stack.append(i)
print(*result)