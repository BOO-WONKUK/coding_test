from collections import deque
def solution(x, y, n):
    dp = [float('inf')] * (y + 1)
    dp[x] = 0
    queue = deque([(x, 0)])

    while queue:
        current, cnt = queue.popleft()
        if current == y:
            return cnt
        for next_pos in [current + n, current * 2, current * 3]:
            if next_pos <= y and dp[next_pos] > cnt + 1:
                dp[next_pos] = cnt + 1
                queue.append((next_pos, cnt + 1))
    
    return -1 if dp[y] == float('inf') else dp[y]
