import sys
input = sys.stdin.readline

n, m = map(int, input().split())
point = list(map(int, input().split()))
plus_point = []
minus_point = []
max = 0

for i in point:
    if i > 0:
        plus_point.append(i)
    else:
        minus_point.append(i)

    if abs(i) > abs(max):
        max = i

plus_point.sort(reverse=True)
minus_point.sort()

walk = 0

for j in range(0, len(plus_point), m):
    if plus_point[j] != max:
        walk += plus_point[j]

for k in range(0, len(minus_point), m):
    if minus_point[k] != max:
        walk += abs(minus_point[k])

walk *= 2
walk += abs(max)

print(walk)
