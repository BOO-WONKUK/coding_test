import heapq
n = int(input())
lst = []
sum = 0
for _ in range(n):
    heapq.heappush(lst, int(input()))

while 1:
    if len(lst) == 1:
        print(sum)
        exit()
    a= heapq.heappop(lst)
    b= heapq.heappop(lst)
    sum += (a+b)
    
    heapq.heappush(lst, a+b)
    
    
