def solve(N, R):
    ans = 0
    P = N - R

    for i in range(1, int(P ** (1 / 2)) + 1):
        if P % i == 0:
            if i > R: ans += i
            if i * i != P and P // i > R:
                ans += P // i
    return ans


N, R = map(int, input().split())
print(solve(N, R))
