import sys
input = sys.stdin.readline

def z(x,y,n):
    global count
    if x>r or x+n <= r or y>c or y+n <= c:
        count += n**2
        return

    if n > 2:
        n //= 2
        z(x,y,n)
        z(x,y+n,n)
        z(x+n,y,n)
        z(x+n,y+n,n)
    else:
        if x==r and y == c:
            print(count)
        elif x==r and y+1 == c:
            print(count+1)
        elif x+1 == r and y==c:
            print(count+2)
        else:
            print(count+3)
        exit()

n, r, c = map(int, input().split())
count = 0
z(0,0,2**n)
