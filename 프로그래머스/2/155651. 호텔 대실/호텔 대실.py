def solution(book_time):
    def change_time(s):
        h,m = map(int, s.split(':'))
        t = h* 60 + m
        return t
    answer = 0
    book_time.sort(key = lambda x :  change_time(x[0]))
    lst_useroom = []
    for s,e in book_time:
        ts, te = change_time(s), change_time(e)
        tmp = -1
        for idx,i in enumerate(lst_useroom):
            if i + 10 <= ts:
                tmp = 1
                lst_useroom[idx] = te
                break
        if tmp == -1:
            lst_useroom.append(te)
    answer = len(lst_useroom)
    
    return answer
