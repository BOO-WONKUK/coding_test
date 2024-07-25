n, m = map(int, input().split())
lst = list(map(int, input().split()))
n_lst = []
tmp = 0
for i in lst:
    tmp += i
    n_lst.append(tmp)
for _ in range(m):
    a,b = map(int, input().split())
    if a ==1 :
        print(n_lst[b-1])
        continue
    print(n_lst[b-1] - n_lst[a-2])
