n = int(input())
nlst = list(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))
nlst.sort()

def func(nlst,x):
    start = 0
    end = n-1

    while start <= end:
        midi = (start+end)//2
        
        if nlst[midi] == x:
            return 1
        elif nlst[midi] > x:
            end = midi - 1
        else:
            start = midi + 1
        
    return 0



results = [func(nlst,x) for x in mlst]

print(" ".join(map(str, results)))