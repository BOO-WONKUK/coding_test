lst = []
while 1:
    s = input()
    if s == '.':
        break
    lst.append(s)

for i in lst:
    b_lst = []
    
    for x in i:
        tmp = -1
        try:
            if x == '[':
                b_lst.append(1)
            elif x == ']':
                x = b_lst.pop()
                if x == 2:
                    tmp = 1
            elif x == '(':
                b_lst.append(2)
            elif x == ')':
                y = b_lst.pop()
                if y == 1:
                    tmp = 1
        except:
            tmp = 1
        if tmp == 1:
            break
    if len(b_lst) == 0 and tmp != 1:
        print('yes')
    else:
        print('no')