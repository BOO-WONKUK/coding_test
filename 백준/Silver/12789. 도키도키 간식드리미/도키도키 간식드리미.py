n = int(input())
line = list(map(int, input().split()))

stack = []
num = 1

while line or stack:
    if line and line[0] == num:
        line.pop(0)
        num += 1
    elif stack and stack[-1] == num:
        stack.pop()
        num += 1
    elif line:
        stack.append(line.pop(0))
    else:
        break

if num - 1 == n:
    print("Nice")
else:
    print("Sad")
