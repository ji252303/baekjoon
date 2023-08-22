import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

#find 연산
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

#합집합 연산
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    op, a, b = map(int,input().split())
    if op == 0:
        union_parent(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
