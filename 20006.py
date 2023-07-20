import sys
input = sys.stdin.readline

p, m = map(int,input().split())
room = []

for p in range(p):
    l, n = input().split()
    if not room:
        room.append([[int(l),n]])
        continue

    enter = False

    for i in room:
        if len(i) < m and i[0][0] - 10 <= int(l) <= i[0][0] + 10:
            i.append([int(l),n])
            enter = True
            break
    if not enter:
        room.append([[int(l),n]])

for i in room:
    i.sort(key=lambda x:x[1])

for i in room:
    if len(i) == m:
        print('Started!')
    else:
        print('Waiting!')
    for lev, name in i:
        print(lev, name)
