def solution(participant, completion):
    answer = ''
    dict = {}
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in completion:
        if i in dict:
            dict[i] -= 1
    for k,v in dict.items():
        if v != 0:
            return k
    return answer