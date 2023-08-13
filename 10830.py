import sys
input = sys.stdin.readline

n, b = map(int,input().split())
a = [[*map(int, input().split())] for _ in range(n)]

def multi(u, v):
    n = len(u)
    z = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += u[row][i] * v[i][col]
            z[row][col] = e % 1000

    return z

def square(a, b):
    if b == 1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= 1000
        return a

    temp = square(a, b//2)

    if b % 2:
        return multi(multi(temp,temp),a)
    else:
        return multi(temp,temp)

result = square(a,b)
for z in result:
    print(*z)
