n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

d = [0]*n

d[0] = lst[0]
if n > 1:
    d[1] = lst[0]+lst[1]

if n > 2:
    d[2] = max(lst[2]+lst[1], lst[2]+lst[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+lst[i-1]+lst[i], d[i-2]+lst[i])

print(d[n-1])