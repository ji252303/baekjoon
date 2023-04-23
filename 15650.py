import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list = [i for i in range(0, n+1)]

index = 0
visited = [False] * (len(list)+1)


def backtrack(result):

    if len(result) == m:
        print(*result)
        return

    for i in range(1, n+1):
        if(visited[i] == False) and (len(result) == 0 or i > result[-1]):
            visited[i] = True
            result.append(list[i])
            backtrack(result)
            visited[i] = False
            result.pop()

backtrack([])
