n = int(input())
m = int(input())

pos = list(map(int,input().split()))
len_pos = len(pos)

min_height = 0

if len_pos == 1:
    min_height = max(pos[0] - 0, n - pos[0])
    
else:
    for i in range(len_pos):
        if i == 0:
            height = pos[i] - 0
        elif i == len_pos - 1:
            height = n - pos[i]
        else:
            temp = pos[i] - pos[i-1]
            if temp % 2:
                height = temp//2 + 1
            else:
                height = temp //2
        min_height = max(height, min_height)
    
print(min_height)
            
