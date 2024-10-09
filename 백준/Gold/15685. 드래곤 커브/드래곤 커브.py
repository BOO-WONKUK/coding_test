n = int(input())
lst_command = [list(map(int, input().split())) for _ in range(n)]

# 방향 배열 (0: →, 1: ↑, 2: ←, 3: ↓)
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
result = [[0 for _ in range(101)] for _ in range(101)]

# 좌표 범위 확인 함수
def in_range(x, y):
    return 0 <= x <= 100 and 0 <= y <= 100

# 정사각형의 개수 세기 함수
def check_box():
    ans = 0
    for i in range(100):
        for j in range(100):
            if result[i][j] == 1 and result[i+1][j] == 1 and result[i][j+1] == 1 and result[i+1][j+1] == 1:
                ans += 1
    return ans

# 드래곤 커브 저장 함수
def save_result(x, y, d, g):
    # 현재 좌표를 1로 표시
    result[x][y] = 1
    # 방향 기록 리스트
    history = [d]
    # 첫 방향으로 이동
    x, y = x + dx[d], y + dy[d]
    result[x][y] = 1

    # g 세대만큼 반복
    for _ in range(g):
        # 현재까지 기록된 방향을 역순으로 시계 방향 90도 회전
        for i in reversed(history):
            nd = (i + 1) % 4
            x, y = x + dx[nd], y + dy[nd]
            if in_range(x, y):
                result[x][y] = 1
            history.append(nd)

# 입력 받은 드래곤 커브 처리
for x, y, d, g in lst_command:
    save_result(x, y, d, g)

# 결과 출력
print(check_box())
