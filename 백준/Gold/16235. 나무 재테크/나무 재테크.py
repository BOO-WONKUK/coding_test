from collections import deque

n, m, k = map(int, input().split())
yang = [[5] * n for _ in range(n)]  # 처음 양분은 모든 칸에 5
yang_plus = [list(map(int, input().split())) for _ in range(n)]  # 겨울에 추가될 양분
trees = [[deque() for _ in range(n)] for _ in range(n)]  # 나무 리스트를 deque로 관리

# 초기 나무 정보 입력
for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)  # 나무 나이를 저장 (0-based 좌표)

# 방향 설정 (가을 번식 시 8방향 이동)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_range(r, c):
    return 0 <= r < n and 0 <= c < n

def simulate():
    # 1. 봄: 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가
    dead_nutrients = [[0] * n for _ in range(n)]  # 죽은 나무가 남긴 양분
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                new_trees = deque()
                while trees[i][j]:
                    age = trees[i][j].popleft()
                    if yang[i][j] >= age:
                        yang[i][j] -= age  # 나무가 양분을 먹고
                        new_trees.append(age + 1)  # 나이 1 증가
                    else:
                        dead_nutrients[i][j] += age // 2  # 죽은 나무가 양분으로 변환
                trees[i][j] = new_trees

    # 2. 여름: 죽은 나무가 남긴 양분을 땅에 추가
    for i in range(n):
        for j in range(n):
            yang[i][j] += dead_nutrients[i][j]

    # 3. 가을: 나무 번식 (나이가 5의 배수인 나무만 번식)
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for dr, dc in directions:
                        nr, nc = i + dr, j + dc
                        if is_range(nr, nc):
                            trees[nr][nc].appendleft(1)  # 번식한 나무는 나이가 1인 나무

    # 4. 겨울: 양분 추가
    for i in range(n):
        for j in range(n):
            yang[i][j] += yang_plus[i][j]

# 시뮬레이션 실행
for _ in range(k):
    simulate()

# 나무 개수 세기
result = 0
for i in range(n):
    for j in range(n):
        result += len(trees[i][j])

print(result)
