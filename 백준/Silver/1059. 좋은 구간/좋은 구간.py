import sys
l = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
lst.sort()
if n in lst: 
    print(0)
else:
    left_value, right_value = 0, 0
    for num in lst:
        if num < n: 
            left_value = num
        elif num > n and right_value == 0: 
            right_value = num
    left_value += 1 
    right_value -= 1
    print((n-left_value)*(right_value-n+1)+(right_value-n)) #5