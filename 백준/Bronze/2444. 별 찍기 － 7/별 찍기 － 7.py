n = int(input())

blank = n-1
star = 1

for i in range(n*2 - 1):
    print(' ' * blank, '*' * star, sep = '')
    if i < n -1:
        star += 2
        blank -= 1
    else:
        star -= 2
        blank += 1
        