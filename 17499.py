import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ar = list(map(int, input().split()))

point = 0

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        ar[(point+query[1]-1)%n] += query[2]
    elif query[0] == 2:
        point -= query[1]
    else:
        point += query[1]

for i in range(point, point+n):
    print(ar[i%n], end=' ')
