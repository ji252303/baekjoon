import heapq
import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    k = int(input())
    maxh, minh = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()
        num = int(num)

        if com == 'I':
            heapq.heappush(minh, (num, j))
            heapq.heappush(maxh, (-num, j))
            visited[j] = True

        elif num == 1:
            while maxh and not visited[maxh[0][1]]:
                heapq.heappop(maxh)
            if maxh:
                visited[maxh[0][1]] = False
                heapq.heappop(maxh)
        else:
            while minh and not visited[minh[0][1]]:
                heapq.heappop(minh)
            if minh:
                visited[minh[0][1]] = False
                heapq.heappop(minh)

    while minh and not visited[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not visited[maxh[0][1]]:
        heapq.heappop(maxh)

    print(-maxh[0][0], minh[0][0]) if maxh and minh else print("EMPTY")
