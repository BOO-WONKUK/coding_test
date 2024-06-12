lst = [i for i in range(1, 31)]
for _ in range(28):
    lst[int(input())-1] = 0
for i in range(30):
    if lst[i] != 0:
        print(i+1)