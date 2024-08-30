n = int(input())
lst = [list(map(int, list(input().strip()))) for _ in range(n)]

def func(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if lst[x][y] != lst[i][j]:
                print("(", end="")
                func(x, y, n // 2)
                func(x, y + n // 2, n // 2)
                func(x + n // 2, y, n // 2)
                func(x + n // 2, y + n // 2, n // 2)
                print(")", end="")
                return

    print(1 if lst[x][y] == 1 else 0, end="")

func(0, 0, n)