n = int(input())
sum = 0
lst = set()
for _ in range(n):
    a = input()
    
    if a != 'ENTER':
        lst.add(a)
    else:
        sum += (len(lst))
        lst = set()
        
sum += (len(lst))
print(sum)