def min_cost(N, M, lst):
    min_pkg = min(lst, key=lambda x: x[0])[0]
    min_sgl = min(lst, key=lambda x: x[1])[1]
    
    a = (N // 6) * min_pkg + (min_pkg if N % 6 != 0 else 0)
    b = (N // 6) * min_pkg + (N % 6) * min_sgl
    tmp = N * min_sgl
    
    return min(a, b, tmp)

N, M = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(M)]

print(min_cost(N, M, lst))
