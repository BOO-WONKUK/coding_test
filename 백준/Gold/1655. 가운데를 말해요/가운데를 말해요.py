import sys
import heapq

cnt = int(sys.stdin.readline())
left, right = [], [] 

for i in range(cnt):
  num = int(sys.stdin.readline())
  
  if len(left) == len(right):
    heapq.heappush(left, (-num, num))
  else:
    heapq.heappush(right, (num, num))

  if i > 0 and left[0][1] > right[0][1]:
    temp_l = heapq.heappop(left)[1]
    temp_r = heapq.heappop(right)[1]
    heapq.heappush(left, (-temp_r, temp_r))
    heapq.heappush(right, (temp_l, temp_l))

  print(left[0][1])