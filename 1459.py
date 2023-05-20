import sys
input = sys.stdin.readline

answer = 0

x, y, w, s = map(int, input().split())

if 2*w <= s:
    print((x+y)*w)
else:
    small = min(x, y)
    answer = small * s
    xy = abs(x-y)
    if w > s:
        if xy % 2 == 0:
            answer += xy * s
        else:
            answer += (xy-1)*s + w
    else:
        answer += xy * w
    print(answer)

    
