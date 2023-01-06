n,k = map(int,input().split())
cointype = []

for i in range(n):
    cointype.append(int(input()))

ct = 0

for i in reversed(range(n)):
    ct += k // cointype[i]
    k %= cointype[i]

print(ct)
