import sys
input = sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

dp = [0]*(n+1)
for x in range(1, n+1):
    dp[x] = dp[x-1] + arr[x-1]
for _ in range(m):
    i,j=map(int,input().split())
    print(dp[j]-dp[i-1])
