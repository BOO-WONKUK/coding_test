import heapq
n = int(input())

lst = []

for _ in range(n):
    a = input()
    if a == '0':
        if len(lst) == 0:
            print(-1)
        else:
            print(-heapq.heappop(lst))
        continue
    else:
        k = list(map(int,a.split()))[1:]
        for i in k:
            heapq.heappush(lst,-i)