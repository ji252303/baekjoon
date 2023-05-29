n = int(input())

dp = [0] * (n+1)
point = [0] * (n+1)

for i in range(1, n+1):
    point[i] = int(input())

if n == 1:
    print(point[1])
    exit()
elif n == 2:
    print(sum(point[:3]))
    exit()

dp[1] = point[1]
dp[2] = point[1] + point[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i])

print(dp[-1])
