n= int(input())
start = list(map(int, input()))
target = list(map(int, input()))

def change(a, b):
    a_copy = a[:]
    press = 0
    for i in range(1, n):
        if a_copy[i-1] == b[i-1]:
            continue
        press += 1
        for j in range(i-1,i+2):
            if j < n:
                a_copy[j] = 1 - a_copy[j]
    if a_copy == b:
        return press
    else:
        return 1e9

res = change(start, target)
start[0] = 1 - start[0]
start[1] = 1 - start[1]
res = min(res, change(start, target) + 1)  #시작지점 고려
if res != 1e9:
    print(res)
else:
    print(-1)

