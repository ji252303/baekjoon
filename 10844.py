import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n+1)]

# 1의 자릿수의 경우의 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        # 가장 뒤에 오는 숫자가 0일 땐, 그 앞에 1만
        if (j == 0):
            dp[i][j] = dp[i-1][1]

        # 가장 뒤에 오는 숫자가 1~8일 땐, 그 앞에 +-1
        elif (1 <= j <= 8):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

        # 가장 뒤에 오는 숫자가 9일 땐, 그 앞에 8
        else:
            dp[i][j] = dp[i-1][8]

print(sum(dp[n]) % 1000000000)
