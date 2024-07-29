import sys
input = sys.stdin.readline
n = int(input())
st = set()
for _ in range(n):
    a,b = input().split()
    if b == 'enter':
        st.add(a)
    elif b == 'leave':
        st.remove(a)
lst = list(st)
lst.sort(reverse=True)
for k in lst:
    print(k)

