from collections import deque

def solution(tickets):
    answer = []
    q = deque([["ICN",tickets, []]])
    tickets.sort(key = lambda x : (x[0],x[1]))
    while q:
        city, lst_tickets, lst_ans = q.popleft()
        if len(lst_tickets) == 0:
            lst_ans.append(city)
            return lst_ans
        # answer.append(city)
        # lst_del = []
        for idx,kk in enumerate(lst_tickets):
            a,b = kk[0], kk[1]
            copy_lst_tickets = lst_tickets[:]
            copy_lst_ans = lst_ans[:]
            if city == a:
                copy_lst_tickets.pop(idx)
                copy_lst_ans.append(city)
                q.append([b, copy_lst_tickets, copy_lst_ans])
                # lst_del.append(idx)
                
    return lst_ans