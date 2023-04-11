import sys

input = sys.stdin.readline

N, K= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key= lambda x : (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if arr[i][0] == K:
        id = i

for i in range(N):
    if arr[id][1:] == arr[i][1:]:
        print(i+1)
        break
