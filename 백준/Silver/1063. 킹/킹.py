move = {"R" : (0, 1), "L" : (0, -1), "B" : (1, 0), "T" : (-1, 0),
"RT" : (-1, 1), "LT" : (-1, -1), "RB" : (1, 1), "LB" : (1, -1)}

k, s, n = map(str, input().split())
k_x = 8 - int(k[1])
k_y = ord(k[0]) - 65

s_x = 8 - int(s[1])
s_y = ord(s[0]) - 65

for _ in range(int(n)):
    m = input()
    if 0 <= k_x + move[m][0] < 8 and 0 <= k_y + move[m][1] < 8:
        if k_x + move[m][0] == s_x and k_y + move[m][1] == s_y:    
            if 0 <= s_x + move[m][0] < 8 and 0 <= s_y + move[m][1] < 8:
                k_x = k_x + move[m][0]
                k_y = k_y + move[m][1]
                s_x = s_x + move[m][0]
                s_y = s_y + move[m][1]
            else:
                continue

        else:
            k_x = k_x + move[m][0]
            k_y = k_y + move[m][1]
    else:
        continue

print(chr(k_y + 65), str(8 - k_x), sep = "")
print(chr(s_y + 65), str(8 - s_x), sep = "")