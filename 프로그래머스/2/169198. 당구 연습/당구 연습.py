def solution(m, n, startX, startY, balls):
    answer = []
    half_x = m/2
    half_y = n/2
    for i, j in balls:
        lst = []
        if not (startX >= i and startY ==j):
            lst.append(((-startX -i) ** 2 + (startY - j) ** 2) )
        if not (startX <= i and startY ==j):
            lst.append(((2*m-startX -i) ** 2 + (startY - j) ** 2) )
        if not (startX == i and startY >=j):
            lst.append(((startX -i) ** 2 + (-startY - j) ** 2) )
        if not (startX == i and startY <=j):
            lst.append(((startX -i) ** 2 + (2*n - startY - j) ** 2) )
        answer.append(min(lst))
    return answer