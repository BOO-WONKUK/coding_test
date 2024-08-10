n, m = tuple(map(int, input().split()))
lst = []
for _ in range(n):
    lst.append(input())
    
k = int(input())

max_cnt = 0

for col in range(n):
    z_cnt = 0
    for num in lst[col]:
        if num == '0':
            z_cnt += 1
        
    col_cnt = 0
    if z_cnt <= k and z_cnt % 2 == k % 2: 
        for col2 in range(n):  
            if lst[col] == lst[col2]: 
                col_cnt += 1 
                
    max_cnt = max(max_cnt, col_cnt) 
    
print(max_cnt)