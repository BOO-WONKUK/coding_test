n = int(input())
def func(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        func(n-1, a, c, b) 
        print(a, c)
        func(n-1, b, a, c)
sum = 2 ** n - 1
print(sum)

func(n, 1, 2, 3)