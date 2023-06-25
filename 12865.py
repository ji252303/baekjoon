def knapsack(N, K, weights, values):
    # DP 테이블 초기화
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    # 물건들을 하나씩 고려하여 DP 테이블 업데이트
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            # i번째 물건을 배낭에 넣을 수 있는 경우
            if weights[i] <= j:
                dp[i][j] = max(values[i] + dp[i - 1][j - weights[i]], dp[i - 1][j])
            # i번째 물건을 배낭에 넣을 수 없는 경우
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N][K]

# 입력 받기
N, K = map(int, input().split())
weights = [0]
values = [0]

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# 문제 해결 및 결과 출력
answer = knapsack(N, K, weights, values)
print(answer)
