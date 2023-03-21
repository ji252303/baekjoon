import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = input().strip()
    b = int(input())
    flag = 1
    arr = input().strip()
    dq = deque(arr[1:-1].split(','))
    if b == 0:
        dq = deque()
    R = 0
    for i in range(len(a)):
        if a[i] == 'R':
            R += 1
        elif a[i] == 'D':
            if len(dq) == 0:
                print('error')
                flag= 0
                break
            else:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()

    if flag == 0:
        continue
    else:
        if R % 2 == 0:
            print('[' + ",".join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ",".join(dq) + ']')
