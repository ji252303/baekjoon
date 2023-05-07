import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = set()

for i in range(n):
    s.add(input())
    
answer = 0

for _ in range(m):
    t = input()
    if t in s:
        answer += 1
    
print(answer)
