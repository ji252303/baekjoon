import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    num_list = list(map(int, input().split()))
    if not q:
        for j in num_list:
            heapq.heappush(q, j)
    else:
        for k in num_list:
            if q[0] < k:
                heapq.heappush(q, k)
                heapq.heappop(q)

print(q[0])
