def solution(k, tangerine):
    answer = 0
    lst = []
    check = [0]*10000001
    for i in tangerine:
        check[i] += 1
    # lst.sort(key = lambda x : x)
    check.sort(reverse = True)
    print(lst)
    # for j in range(len(lst)-1, -1 ,-1):
    for cnt in check:
        # cnt = lst[j]
        if cnt >= k:
            answer += 1
            return answer
        else:
            k -= cnt
            answer += 1
    
    return answer