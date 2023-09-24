import sys

input = sys.stdin.readline

def solve(n,i,j):
    if n == 0:
        return

    count = (j-i+1) // 3
    solve(n-1, i, i+count + 1) #왼쪽
    for k in range(i+count, i+count*2):
        answer[k] = ' '
    solve(n-1, i+count * 2, i + count*3 - 1)



while True:
    try:
        n = int(input())
        answer = ['-'] * (3 ** n)
        solve(n,0, 3 ** n-1)
        print(''.join(answer))
    except:
        break
