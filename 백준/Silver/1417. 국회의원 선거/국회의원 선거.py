n = int(input())
k = int(input())  
lst = [] 
cnt = 0

for _ in range(n - 1):
    lst.append(int(input()))

if n == 1:
    print(0)
    exit()

while k <= max(lst):
    lst[lst.index(max(lst))] -= 1
    k += 1
    cnt += 1

print(cnt)