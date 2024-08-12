import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    tmp = list(sys.stdin.readline().split())
    lst.append(tmp[1:])
    
lst.sort()

for j in range(len(lst[0])):
    print("--" * j + lst[0][j])
    
for i in range(1, n):
    count = -1
    for j in range(len(lst[i])):
        if len(lst[i - 1]) <= j or lst[i - 1][j] != lst[i][j]:
            break
        else:
            count = j
            
    for j in range(count + 1, len(lst[i])):
        print("--" * j + lst[i][j])