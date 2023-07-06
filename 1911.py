import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x:x[0])
last = 0
count = 0

for start, end in lst:
    if start > end:
        continue
    if last > start:
        start = last
    while start < end:
        start += l
        count += 1
    last = start

print(count)
 //위는 시간초과 코드..

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x:x[0])
last = 0
res = 0

for start, end in lst:
    last = max(start, last)
    diff = end - last
    count = (diff + l - 1) // l
    res += count
    last += count * l

print(res)
