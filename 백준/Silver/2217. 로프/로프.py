n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
ans = []
for i in range(n):
    ans.append(lst[i] * (n - i))
print(max(ans))