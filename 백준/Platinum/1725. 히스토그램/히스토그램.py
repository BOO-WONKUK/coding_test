import sys
input = sys.stdin.readline

def func(hist):
    s = []
    max_area = 0
    idx = 0
    
    while idx < len(hist):
        if not s or hist[idx] >= hist[s[-1]]:
            s.append(idx)
            idx += 1
        else:
            top = s.pop()
            area = hist[top] * ((idx - s[-1] - 1) if s else idx)
            max_area = max(max_area, area)
    
    while s:
        top = s.pop()
        area = hist[top] * ((idx - s[-1] - 1) if s else idx)
        max_area = max(max_area, area)
    
    return max_area

n = int(input())
hist = [int(input()) for _ in range(n)]

print(func(hist))
