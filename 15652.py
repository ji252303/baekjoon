n, m = map(int,input().split())
lst = [0] * m

def backtrack(k):
    if k == m:
        print(*lst)
        return
    start = 1
    if k != 0:
        start = lst[k-1]
    for i in range(start, n+1):
        lst[k] = i
        backtrack(k+1)
        
backtrack(0)
