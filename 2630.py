import sys
input = sys.stdin.readline

n= int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
answer = [0, 0]

def cut(x, y, n):
    color = paper[x][y]
    for row in range(x, x+n):
        for col in range(y, y+n):
            if color != paper[row][col]:
                cut(x, y,  n//2)
                cut(x, y+n//2, n // 2)
                cut(x+n//2, y, n // 2)
                cut(x+n//2, y+n//2, n // 2)
                return 0
    if color == 0:
        answer[0] += 1
    else:
        answer[1] += 1

cut(0, 0, n)
for i in answer:
    print(i)

