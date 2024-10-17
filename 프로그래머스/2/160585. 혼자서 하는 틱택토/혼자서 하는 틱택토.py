def solution(board):
    answer = -1
    x_cnt = 0
    o_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x_cnt += 1
            elif board[i][j] == 'O':
                o_cnt += 1
                
    if o_cnt < x_cnt :      # 선후공 규칙 안지킴
        return 0
    if o_cnt - 2 >= x_cnt:
        return 0
    # 이미 끝났어도 진행 / 가로 3개
    for s in board:         
        if s == 'OOO' and x_cnt + 1 != o_cnt:
            return 0
        elif s == 'XXX' and x_cnt != o_cnt:
            return 0
    # 세로 3개
    for j in range(3):
        x_se_cnt = 0
        o_se_cnt = 0
        for i in range(3):
            if board[i][j] == 'O':
                o_se_cnt += 1
            elif board[i][j] == 'X':
                x_se_cnt += 1
        if x_se_cnt == 3 and x_cnt != o_cnt:
            return 0
        elif o_se_cnt == 3 and x_cnt + 1 != o_cnt:
            return 0
    # 대각선 -> /
    x_se_cnt1 = 0
    o_se_cnt1 = 0
    x_se_cnt2 = 0
    o_se_cnt2 = 0
    for j in range(3):
        for i in range(3):
            if i == j:
                if board[i][j] == 'O':
                    o_se_cnt1 += 1
                elif board[i][j] == 'X':
                    x_se_cnt1 += 1
            if (i == 0 and j == 2) or ( i == 1 and j == 1) or (i == 2 and j == 0):
                if board[i][j] == 'O':
                    o_se_cnt2 += 1
                elif board[i][j] == 'X':
                    x_se_cnt2 += 1
    if x_se_cnt1 == 3 and x_cnt != o_cnt:
        return 0
    elif o_se_cnt1 == 3 and x_cnt + 1 != o_cnt:
        return 0
    if x_se_cnt2 == 3 and x_cnt != o_cnt:
        return 0
    elif o_se_cnt2 == 3 and x_cnt + 1 != o_cnt:
        return 0

    return 1