s = input()
if len(s)%2==1 and s[:len(s)//2] == s[len(s)//2+1:][::-1]:
    print(1)
elif len(s)%2==0 and s[:len(s)//2] == s[len(s)//2:][::-1]:
    print(1)
else:
    print(0)
    