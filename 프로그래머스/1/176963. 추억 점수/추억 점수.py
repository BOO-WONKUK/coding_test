def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        result = 0
        for j in photo[i]:
            if j in name:
                result += yearning[name.index(j)]
        answer.append(result)
    return answer