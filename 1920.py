import sys
input = sys.stdin.readline

a = int(input())
b = set(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))

for num in d:
    print(1) if num in b else print(0)
