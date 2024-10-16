def solution(diffs, times, limit):
    answer = 0
    l = len(diffs)
    min_ = 1
    max_ = max(diffs)
    
    while min_ < max_:
        mid = (min_ + max_) // 2
        result = 0
        
        for i in range(len(diffs)):
            if i == 0:
                time_prev = 0
            else:
                time_prev = times[i-1]
            
            if diffs[i] <= mid:
                result += times[i]
            else:
                result += (diffs[i] - mid) * (times[i] + time_prev) + times[i]
            
        if result > limit:
            min_ = mid + 1
        else:
            max_ = mid
    
    return min_