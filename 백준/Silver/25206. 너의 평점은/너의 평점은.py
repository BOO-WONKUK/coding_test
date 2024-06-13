sum = 0
ssum = 0
cnt = 0
for _ in range(20):
    _, n, s = map(str, input().split())
    if s != 'P':
        if s == 'A+':
            sum += float(n)*4.5
        elif s == 'A0':
            sum += float(n)*4
        elif s == 'B+':
            sum += float(n)*3.5
        elif s == 'B0':
            sum += float(n)*3
        elif s == 'C+':
            sum += float(n)*2.5
        elif s == 'C0':
            sum += float(n)*2
        elif s == 'D+':
            sum += float(n)*1.5
        elif s == 'D0':
            sum += float(n)*1
        elif s == 'F':
            sum += float(n)*0

        ssum += float(n)
    
print('{:.4f}'.format(sum/ssum))