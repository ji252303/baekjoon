import sys
input = sys.stdin.readline

n, c = map(int,input().split())
h = [int(input()) for i in range(n)]
h.sort()
start = 1
end = h[n-1] - h[0]
result = 0

if c == 2:
    print(h[n-1]-h[0])
else:
    while(start < end):
        mid = (start+end)//2
        count = 1
        t = h[0]
        #공유 마지막설치 위치
        
        for i in range(n):
            if h[i] - t >= mid:
                count += 1
                t = h[i]
        if count >= c:
            result = mid
            start = mid + 1
        else:
            end = mid
    print(result)
