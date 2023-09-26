import sys
input = sys.stdin.readline

x, y = map(int,input().rsplit())
vic = y * 100 // x
answer = sys.maxsize
start, end = 1, x


while start <= end:
    mid = (start+end) // 2
    cur = (y+mid) * 100 // (x + mid)

    if cur > vic:
        answer = min(mid,answer)
        end = mid - 1
    else:
        start = mid + 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
