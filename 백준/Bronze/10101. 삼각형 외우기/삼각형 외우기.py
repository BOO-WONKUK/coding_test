lst = []
sum= 0
for i in range(3):
    n = int(input())
    lst.append(n)

for i in lst:
    sum += i

if sum == 180:
    if lst[0]!= lst[1] and lst[1]!=lst[2] and lst[0]!=lst[2]:
        print("Scalene")
    elif lst[0] == 60 and lst[1] == 60 and lst[2] ==60 : 
        print("Equilateral")
    else: print("Isosceles")

else: 
    print("Error")