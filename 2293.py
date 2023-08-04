import sys
input = sys.stdin.readline

n, k = [*map(int,input().split())]
coin = [int(input()) for _ in range(n)]

dp = [1] + [0]*k
# dp[i] -> i원을 만들 때 가능한 경우의 수
# dp[0] -> 동전 하나를 사용하는 경우 (coin이 3일 때, dp[3 - 3] = 1로 맞춰줌으로써 0원에서 3원을 더해 3원을 만드는 경우라고 생각)

for i in coin:
    # coin원 동전으로 i원 만들기 -> i - coin원을 만든 후 coin원을 추가하는 것과 같음
    # 즉, coin원으로 동전을 만드는 경우의 수 -> dp[i - coin]원
    for col in range(i,k+1):
        dp[col] += dp[col-i]

print(dp[k])
