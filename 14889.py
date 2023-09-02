import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [False for _ in range(n)]
min_value = sys.maxsize

def back(dep, idx):
    global min_value
    if dep == n // 2:
        power1,power2 = 0,0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]:
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1-power2))
        return

    for i in range(idx,n):
        if not visit[i]:
            visit[i] = True
            back(dep + 1, i+1)
            visit[i] = False

back(0,0)
print(min_value)

