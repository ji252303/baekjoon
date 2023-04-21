import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
rank = []
power = []

for _ in range(n):
    a, b = input().split()
    rank.append(a)
    power.append(int(b))


for _ in range(m):
    print(rank[bisect_left(power, int(input()))])
