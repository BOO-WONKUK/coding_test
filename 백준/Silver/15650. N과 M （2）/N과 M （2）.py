import itertools

def func(N, M):
    num = list(range(1, N + 1))
    combinations = itertools.combinations(num, M)
    
    for combination in combinations:
        print(' '.join(map(str, combination)))

N, M = map(int, input().split())
func(N, M)
