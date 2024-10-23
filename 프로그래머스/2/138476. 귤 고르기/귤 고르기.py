def solution(k, tangerine):
    tan_dict = {}
    cnt = 0
    
    for i in set(tangerine):
        tan_dict[i] = 0 # 딕셔너리 생성
    
    for i in tangerine:
        tan_dict[i] += 1 # 딕셔너리에 값 생성, 저장
    
    counts = sorted((i for i in tan_dict.values()), reverse = True) 
    # 개수만 저장 후 sort
    
    for i,j in enumerate(counts): # 인덱스와 같이 for문으로 돌리기
        cnt += j
        if cnt >= k:
            return i+1