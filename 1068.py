n = int(input())
_parent = list(map(int, input().split()))
delete = int(input())
Trees = [[] for _ in range(n+1)]
root = -1 # root 노드 위치 초기화
cnt = 0

def dfs(node):
    global Trees, cnt, delete
    if not Trees[node]:
        cnt += 1
        return

    for j in range(len(Trees[node])):
        if Trees[node][j] == delete:
            if len(Trees[node]) == 1:
                cnt += 1
            else:
                continue
        else:
            dfs(Trees[node][j]) #자식노드를 매개변수로 실행

for i in range(len(_parent)):
    if _parent[i] == -1:
        root = i
    else:
        Trees[_parent[i]].append(i)

if delete == root:
    print(0)
else:
    dfs(root)
    print(cnt)
