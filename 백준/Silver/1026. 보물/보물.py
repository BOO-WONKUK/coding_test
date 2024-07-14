n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sort_a = sorted(a_list, reverse=True)
sort_b = sorted(b_list)

s = 0
for i in range(n):
    s += sort_a[i] * sort_b[i]

print(s)