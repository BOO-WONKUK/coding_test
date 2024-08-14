n,k = map(int, input().split())
lst = list(map(int, input().split()))

result =[]

result.append(sum(lst[:k]))

for i in range(n - k):
    result.append(result[i] - lst[i] + lst[k+i])
        
print(max(result))