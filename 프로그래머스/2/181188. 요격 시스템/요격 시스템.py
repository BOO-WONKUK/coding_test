def solution(targets):
    answer = 0
    cnt = 0
    bound = 0
    for s,e in sorted(targets):
        if bound > s:
            bound = min(bound,e)
        else:
            bound = e
            cnt += 1
        
        
        
        
    return cnt