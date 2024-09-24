n = int(input())  
a = list(map(int, input().split()))  
b, c = map(int, input().split())  

cnt = 0  

for i in range(n):
    cnt += 1
    a[i] -= b
    
    if a[i] > 0:
        cnt += (a[i] + c - 1) // c

print(cnt)
