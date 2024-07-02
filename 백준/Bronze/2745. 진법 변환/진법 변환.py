n, b = input().split()
n = n[::-1]

sum = 0
for i in range(len(n)):
    if ord(n[i]) >=65:
        sum += (ord(n[i])-55)*(int(b)**(i))
    else:
        sum += int(n[i])*(int(b)**(i))
print(sum)