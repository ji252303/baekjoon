import sys
sys.setrecursionlimit(100000)

def star(l):
    d = l//3
    if l == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ["*"]*3
        return

    star(d)

    for i in range(0, l, d):
        for j in range(0,l,d):
            if i != d or j != d:
                for k in range(d):
                    g[i+k][j:j] = g[k][:d]

n = int(sys.stdin.readline().strip())
g = [[' ' for _ in range(n)] for _ in range(n)]

star(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()
