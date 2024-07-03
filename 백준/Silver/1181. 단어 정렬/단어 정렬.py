n = int(input())
lst = set()
for _ in range(n):
    a = input()
    lst.add(a)
ans = []
for i in lst:
    ans.append([i,len(i)])
ans.sort(key = lambda x:(x[1],x[0]))
for x,_ in ans:
    print(x)