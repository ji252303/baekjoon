import sys
input = sys.stdin.readline

def find_sum(N, R):
    total_sum = 0
    for m in range(1, N+1):
        if N % m == R:
            total_sum += m
    return total_sum

# 테스트 예시
N, R = map(int, input().split())
result = find_sum(N, R)
print(result)
