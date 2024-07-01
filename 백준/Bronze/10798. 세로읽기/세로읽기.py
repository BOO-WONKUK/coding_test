a = []
for i in range(5) :
    b = input()
    b= b+ '_'*(15-len(b))
    a.append(b)

for j in range(15) :
    for i in range(5) :
        if a[i][j] != '_' :
            print(a[i][j], end="")