n,b = map(int, input().split())
ans = ''
while n >= b:
    k = n % b
    n = n // b
    if k >9:
        ans += chr(k+55)
    else:
        ans += str(k)
k = n % b
if k >9:
    ans += chr(k+55)
else:
    ans += str(k)
print(ans[::-1])