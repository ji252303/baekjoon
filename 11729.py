n = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
cnt = 0

for _ in range(n):
    cnt = 2 * cnt + 1
print(cnt)
hanoi(n,1,2,3)
