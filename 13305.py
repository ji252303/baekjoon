n = int(input())
km = list(map(int,input().split()))
price = list(map(int,input().split()))

min = price[0]
sum = 0

for i in range(n-1):
    if min>price[i]:
        min=price[i]

    sum +=(min * km[i])
print(sum)
