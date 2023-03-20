import sys
from collections import deque

d = deque()
n = int(input())

for i in range(n):
    com = sys.stdin.readline().split()

    if com[0] == 'push_front':
        d.appendleft(com[1])
    elif com[0] == 'push_back':
        d.append(com[1])
    elif com[0] == 'pop_front':
        if d:
            print(d[0])
            d.popleft()
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if d:
            print(d[len(d)-1])
            d.pop()
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(d))
    elif com[0] == 'empty':
        if d:
            print('0')
        else:
            print('1')
    elif com[0] == 'front':
        if d:
            print(d[0])
        else:
            print('-1')
    elif com[0] == 'back':
        if d:
            print(d[len(d)-1])
        else:
            print('-1')
