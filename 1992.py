import sys
input = sys.stdin.readline

n= int(input())
image = [input().strip() for _ in range(n)]
answer =''

def comp(x,y,n):
    check = image[x][y]
    global answer
    for row in range(x, x+n):
        for col in range(y,y+n):
            if check != image[row][col]:
                answer += '('
                comp(x, y, n // 2)
                comp(x,y+n//2,n//2)
                comp(x+n//2,y,n//2)
                comp(x+n//2,y+n//2,n//2)
                answer += ')'
                return None
    if check == '0':
        answer += '0'
    else:
        answer += '1'
    return None

comp(0,0,n)
print(answer)
