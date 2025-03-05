n = int(input())
tmp = 1
while 1:
    if (n*2) < (tmp**2 + tmp):
        print(tmp-1)
        break
    tmp += 1