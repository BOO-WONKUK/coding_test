def solution(picks, minerals):
    if sum(picks * 5) < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    answer = 0
    lst = []
    tmp_lst = []
    tmp = 0
    cnt = 0
    for s in minerals:
        if cnt % 5 == 0:
            lst.append([tmp_lst,tmp])
            tmp_lst = []
            tmp = 0
        if s == 'diamond':
            tmp += 25
        elif s == 'iron':
            tmp += 5
        else:
            tmp += 1
        cnt += 1
        tmp_lst.append(s)
    print(lst)
    print(tmp_lst)
    if len(tmp_lst) != 0:
        lst.append([tmp_lst, tmp])
        
    lst.pop(0)
    lst.sort(key = lambda x : (-x[1], len(x[0])))
    print(lst)
    
    for i,p in enumerate(picks):
        for _ in range(p):
            if len(lst) == 0:
                return answer
            l = lst[0][0]
            for x in l:
                if x == 'diamond':
                    if i == 0:
                        answer += 1
                    elif i == 1:
                        answer += 5 
                    else:
                        answer += 25
                elif x == 'iron':
                    if i == 2:
                        answer += 5
                    else:
                        answer += 1
                else:
                    answer += 1
            lst.pop(0)
    return answer