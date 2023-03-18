import sys

n = int(input())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

a = sorted(a)

for i in range(len(a)):
    print(a[i])
