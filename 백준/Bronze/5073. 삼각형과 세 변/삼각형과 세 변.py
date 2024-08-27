while 1:
    a,b,c = map(int, input().split())
    if a | b | c :
        if sum([a,b,c])-max(a,b,c) > max(a,b,c):
            if a == b == c:
                print('Equilateral')
            elif a == b or b == c or a == c:
                print('Isosceles')
            elif a != b and b != c and a != c:
                print('Scalene')
        else:
            print('Invalid')
    else:
        exit()