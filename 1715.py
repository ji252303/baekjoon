import heapq
import sys

card = []
result = 0

for i in range(int(sys.stdin.readline())):
    heapq.heappush(card, int(sys.stdin.readline()))

if len(card) == 1:
    print(0)
else:
    while len(card) > 1:
        sum = heapq.heappop(card) + heapq.heappop(card)
        result += sum
        heapq.heappush(card, sum)

    print(result)
