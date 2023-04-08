import sys

n = int(input())
s = set()

for _ in range(n):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    else:
        com, x = temp[0], temp[1]
        x = int(x)

        if com == 'add':
            s.add(x)
        elif com == 'remove':
            s.discard(x)
        elif com == 'check':
            print(1 if x in s else 0)
        elif com == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
