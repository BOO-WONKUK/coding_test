n = int(input())
lst=[2,3]
for i in range(2,n+1):
    lst.append(lst[i-1]*2 -1)
print(lst[n]**2)
    