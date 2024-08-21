n, m = map(int, input().split())

seta = set()
for i in range(n):
    seta.add(input())
setb = set()
for i in range(m):
    setb.add(input())

result = sorted(list(seta & setb))

print(len(result))

for i in result:
    print(i)