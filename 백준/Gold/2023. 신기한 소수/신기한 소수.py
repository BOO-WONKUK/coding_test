from collections import deque

def isprime(n):
    if  n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n= int(input())

cnt = 0 
lst = deque(['2','3','5','7'])
if n == 1:
    for i in lst:
        print(i)
    exit()
for _ in range(n-1):
    for _ in range(len(lst)):
        k = str(lst.popleft())
        
        for j in range(1,10):
            m = k + str(j)
            
            if isprime(int(m)) == True:
                lst.append(int(m))

for i in lst:
    print(i)
