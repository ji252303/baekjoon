import sys
from collections import deque
input = sys.stdin.readline

l = int(input())
ml, mk = map(int, input().split())
c = int(input())
z = [int(input()) for _ in range(l)]

q = deque()

count = 0
answer = True

for i in range(min(ml,l)):
    if count == 0:
        if z[i]-mk*(i+1) <= 0:
            q.append(0)
        else:
            q.append(z[i]-mk*(i+1))
            count += 1
    else:
        if z[i]-mk*(i+1-count) <=0:
            q.append(0)
        else:
            q.append(z[i]-mk*(i+1-count))
            count += 1

for i in range(ml,l):
    if q[0] == 0:
        q.popleft()
        if z[i]-mk*(ml-count) <= 0:
            q.append(0)
        else:
            q.append(z[i]-mk*(ml-count))
            count += 1
    else:
        q.popleft()
        if c > 0:
            c -= 1
        else:
            answer = False
            break
        if z[i]-mk*(ml-count) <= 0:
            q.append(0)
            count -= 1
        else:
            q.append(z[i]-mk*(ml-count))

if answer:
    while q:
        if q[0] == 0:
            q.popleft()
        else:
            q.popleft()
            count -= 1
            if c>0:
                c-= 1
            else:
                answer = False
                break

if answer:
    print('YES')
else:
    print('NO')


