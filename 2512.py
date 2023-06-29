import sys

input = sys.stdin.readline

def number(start, end):
    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for i in arr:
            if i > mid:
                sum += mid
            else:
                sum += i
        if sum <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end
            

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
answer = number(0, max(arr))
print(answer)
