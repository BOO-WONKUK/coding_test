s = input()
a = s.split('1')
b = s.split('0')
cnt_1=0
cnt_2=0
for i in a:
    if i != '':
        cnt_1+=1
for i in b:
    if i != '':
        cnt_2+=1
print(min(cnt_1,cnt_2))