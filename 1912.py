n = int(input())
ar = list(map(int, input().split()))

d = [0] * n
d[0] = ar[0]
for i in range(1, n):
    d[i] = max(ar[i], d[i-1]+ar[i])
print(max(d))
