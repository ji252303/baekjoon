import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    max = stock[0]
    sum = 0

    for i in range(1, n):
        if max < stock[i]:
            max = stock[i]
            continue
        sum += max - stock[i]

    print(sum)
