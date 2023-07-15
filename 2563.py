import sys
input = sys.stdin.readline


n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

result = 0
for row in arr:
    result += row.count(1)
print(result)
