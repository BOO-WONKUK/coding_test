while 1:
    s = int(input())
    lst = []
    if s == -1:
        exit()
    for i in range(1,s):
        if s % i == 0:
            lst.append(i)
    if sum(lst) == s:
        print(s,'=',' + '.join(map(str,lst)))
    else:
        print(s,'is NOT perfect.')