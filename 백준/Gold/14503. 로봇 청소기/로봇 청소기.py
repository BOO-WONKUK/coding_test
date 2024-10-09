
n, m = tuple(map(int, input().split()))
curr_x, curr_y, curr_dir = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]


def can_go(x, y):
    return not grid[x][y] and not visited[x][y]


def simulate():
    global curr_x, curr_y, curr_dir

    visited[curr_x][curr_y] = True

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for _ in range(4):
        left_dir = (curr_dir - 1 + 4) % 4
        next_x = curr_x + dxs[left_dir]
        next_y = curr_y + dys[left_dir]

        if can_go(next_x, next_y):
            curr_x, curr_y = next_x, next_y
            curr_dir = left_dir
            return True

        else:
            curr_dir = left_dir

    back_x = curr_x - dxs[curr_dir]
    back_y = curr_y - dys[curr_dir]

    if not grid[back_x][back_y]:
        curr_x, curr_y = back_x, back_y
        return True
    else:
        return False


while True:
    moved = simulate()

    if not moved:
        break

ans = sum([
    1
    for i in range(n)
    for j in range(m)
    if visited[i][j]
])

print(ans)