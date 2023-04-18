import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b= set()

for _ in range(n):
    name = input().strip()
    a.add(name)

for _ in range(m):
    name = input().strip()
    b.add(name)

result = sorted(list(a & b))

print(len(result), *result, sep='\n')
