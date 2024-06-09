def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        l = ''
        tmp = s[:i]
        cnt = 1
        
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    l += str(cnt) + tmp
                else:
                    l += tmp
                cnt = 1
                tmp = s[j:j+i]
                
        if cnt > 1:
            l += str(cnt) + tmp
        else:
            l += tmp
        answer.append(len(l))
        
    return min(answer)