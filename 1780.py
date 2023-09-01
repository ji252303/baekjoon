import sys
input = sys.stdin.readline


n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

result = {-1:0, 0:0, 1:0}

def divide(row,col,n):
    cur = paper[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            if paper[i][j] != cur:
                next = n//3
                divide(row, col, next)
                divide(row, col + next, next)
                divide(row, col + (next * 2), next)
                divide(row + next, col, next)
                divide(row + next, col + next, next)
                divide(row + next, col + (next * 2), next)
                divide(row + (next * 2), col, next)
                divide(row + (next * 2), col + next, next)
                divide(row + (next * 2), col + (next * 2), next)
                return

    result[cur] += 1
    return

divide(0,0,n)

for i in result.values():
    print(i)
