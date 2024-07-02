n = int(input())
for _ in range(n):
    x = int(input())
    print(x//25,end = ' ')
    x = x%25
    print(x//10,end = ' ')
    x = x%10
    print(x//5,end = ' ')
    x = x%5
    print(x)
    
    