import math

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_average_distance(locations):
    n = len(locations)
    total_distance = 0

    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_distance(locations[i], locations[j])
            total_distance += distance

    average_distance = total_distance * 2 / (n * (n - 1))
    return average_distance

# 입력
N = int(input())
locations = []
for _ in range(N):
    x, y = map(int, input().split())
    locations.append((x, y))

# 평균 이동 거리 계산
result = calculate_average_distance(locations)
result *= 2  # 결과에 2를 곱함

formatted_result = "{:.9f}".format(result)
print(formatted_result)
