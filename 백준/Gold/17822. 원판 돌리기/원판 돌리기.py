# 입력 받기
n, m, t = map(int, input().split())
disks = [list(map(int, input().split())) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(t)]

# 원판 회전 함수
def rotate_disk(disk, direction, k):
    if direction == 0:  # 시계 방향
        disk = disk[-k:] + disk[:-k]
    else:  # 반시계 방향
        disk = disk[k:] + disk[:k]
    return disk

# 인접한 수를 제거하는 함수
def remove_adjacent():
    to_remove = [[False] * m for _ in range(n)]
    found = False

    # 같은 원판 내에서 인접한 숫자 확인
    for i in range(n):
        for j in range(m):
            if disks[i][j] == 0:
                continue
            # 오른쪽 확인
            if disks[i][j] == disks[i][(j+1) % m]:
                to_remove[i][j] = True
                to_remove[i][(j+1) % m] = True
                found = True

    # 서로 다른 원판 간의 인접한 숫자 확인
    for i in range(n-1):
        for j in range(m):
            if disks[i][j] == 0:
                continue
            if disks[i][j] == disks[i+1][j]:
                to_remove[i][j] = True
                to_remove[i+1][j] = True
                found = True

    # 수를 제거
    if found:
        for i in range(n):
            for j in range(m):
                if to_remove[i][j]:
                    disks[i][j] = 0

    return found

# 평균 계산 및 값 조정 함수
def adjust_by_average():
    total_sum = 0
    total_count = 0
    for i in range(n):
        for j in range(m):
            if disks[i][j] != 0:
                total_sum += disks[i][j]
                total_count += 1

    if total_count == 0:
        return

    average = total_sum / total_count
    for i in range(n):
        for j in range(m):
            if disks[i][j] != 0:
                if disks[i][j] > average:
                    disks[i][j] -= 1
                elif disks[i][j] < average:
                    disks[i][j] += 1

# 명령 처리
for x, d, k in commands:
    # 회전
    for i in range(x-1, n, x):
        disks[i] = rotate_disk(disks[i], d, k)
    
    # 인접한 수 제거
    if not remove_adjacent():
        # 인접한 수가 없으면 평균을 기준으로 조정
        adjust_by_average()

# 최종 결과 계산
result = 0
for i in range(n):
    result += sum(disks[i])

print(result)
