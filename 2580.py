import sys
input = sys.stdin.readline

def ch_row(n,x):
    for i in range(9):
        if a[x][i] == n:
            return False
    return True


def ch_col(n,y):
    for i in range(9):
        if a[i][y] == n:
            return False
    return True

def ch_rect(x,y,n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a[nx+i][ny+j] == n:
                return False
    return True

def dfs(count):
    if count == len(zero):
        for i in range(9):
            print(*a[i])
        exit(0)
    x = zero[count][0]
    y = zero[count][1]
    for i in range(1,10):
        if ch_row(i,x) and ch_col(i,y) and ch_rect(x,y,i):
            a[x][y] = i
            dfs(count+1)
            a[x][y] = 0



a = [list(map(int, input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if a[i][j] == 0:
            zero.append([i,j])
dfs(0)
