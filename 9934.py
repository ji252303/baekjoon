def sol(start, end , level):
    if start == end:
        ans[level].append(tree[start])
        return
    center = (start + end) // 2
    ans[level].append(tree[center])
    sol(start, center - 1, level + 1)
    sol(center + 1, end, level + 1)


Level = int(input())
tree = list(map(int, input().split()))
l = len(tree)
ans = [[] for _ in range(Level)]

sol(0, l - 1, 0)
for a in ans:
    print(*a)

