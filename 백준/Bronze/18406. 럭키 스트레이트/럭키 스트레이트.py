n = input()

l = len(n)//2
a = n[:l]
b = n[l:]
tmp_a = 0
tmp_b = 0
for i in a:
    tmp_a += int(i)
    
for i in b:
    tmp_b += int(i)

if tmp_a == tmp_b:
    print('LUCKY')
else:
    print('READY')
    