import sys
from copy import deepcopy

input = sys.stdin.readline
n, m = map(int,input().split())

road = [list(map(int,input().split())) for i in range(n)]

fuel=[[[601 for k in range(3)] for j in range(m)] for i in range(n)]
fuel[0] = deepcopy(road[0])

for i in range(n - 1):
    for j in range(m):
        # 시작점
        if i == 0:
            if j == 0:  # 첫번째 변수
                fuel[i + 1][j][1] = fuel[i][j] + road[i + 1][j]
                fuel[i + 1][j + 1][2] = fuel[i][j] + road[i + 1][j + 1]


            elif j == (m - 1):  # 마지막 변수
                fuel[i + 1][j - 1][0] = fuel[i][j] + road[i + 1][j - 1]
                fuel[i + 1][j][1] = fuel[i][j] + road[i + 1][j]

            else:
                fuel[i + 1][j - 1][0] = fuel[i][j] + road[i + 1][j - 1]
                fuel[i + 1][j][1] = fuel[i][j] + road[i + 1][j]
                fuel[i + 1][j + 1][2] = fuel[i][j] + road[i + 1][j + 1]

        else:
            # 시작점이 아닐 경우.
            if j == 0:
                # 가운데로 내려가는 경우 (3번에서 받은걸로 밖에 못감.)
                fuel[i + 1][j][1] = fuel[i][j][0] + road[i + 1][j]

                # 오른쪽으로 가는 경우. ( 중앙에서 받은거랑 왼쪽에서 받은거 )
                fuel[i + 1][j + 1][2] = min(fuel[i][j][0], fuel[i][j][1]) + road[i + 1][j + 1]

            elif j == (m - 1):
                # 왼쪽으로로 내려간다면 ( 중앙에서 온거 )
                fuel[i + 1][j - 1][0] = min(fuel[i][j][2], fuel[i][j][1]) + road[i + 1][j - 1]

                # 중앙으로 가는 경우 ( 왼 -> 오른쪽으로 온거)
                fuel[i + 1][j][1] = fuel[i][j][2] + road[i + 1][j]

            else:
                # 왼쪽
                fuel[i + 1][j - 1][0] = min(fuel[i][j][1], fuel[i][j][2]) + road[i + 1][j - 1]
                # 가운데
                fuel[i + 1][j][1] = min(fuel[i][j][0], fuel[i][j][2]) + road[i + 1][j]
                # 오른쪽
                fuel[i + 1][j + 1][2] = min(fuel[i][j][0], fuel[i][j][1]) + road[i + 1][j + 1]

result=601
for i in fuel[-1]:
    result=min(result,min(i))
print(result)
