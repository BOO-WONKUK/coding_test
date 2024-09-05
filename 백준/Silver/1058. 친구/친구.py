n = int(input())
lst = [input() for _ in range(n)]
result = [set() for _ in range(n)]
for i in range(n):
    x = lst[i]
    for j in range(n):
        if x[j] == 'Y':
            result[i].add(j)
answer = [0]*n
for i in range(n):
    tmp = set()
    for j in result[i]:
        tmp.add(j)
        for k in result[j]:
            tmp.add(k)
    if i in tmp:
        tmp.remove(i)
    answer[i] += len(tmp)
print(max(answer))