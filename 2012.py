import sys
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))

list.sort()

answer = 0

for i in range(1, n+1):
    answer += abs(i-list[i-1])
print(answer)
