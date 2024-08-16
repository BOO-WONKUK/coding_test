import sys
input = sys.stdin.readline
n = int(input())
lstn = list(map(int, input().split()))
m = int(input())
lstm = list(map(int, input().split()))
dictm = {key:0 for key in lstm}

for i in lstn:
    try:
        if i in dictm:
            dictm[i]+=1
        else:
            continue
    except:
        continue

for j in lstm:
    print(dictm[j],end = ' ')