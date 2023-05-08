import sys
input = sys.stdin.readline

def merge(b):
    if len(b) == 1:
        return b

    mid = (len(b) + 1)//2
    left = merge(b[:mid])
    right = merge(b[mid:])

    b2 = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            b2.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            b2.append(right[j])
            answer.append(right[j])
            j += 1
    
    while i < len(left):
        b2.append(left[i])
        answer.append(left[i])
        i += 1
    
    while j < len(right):
        b2.append(right[j])
        answer.append(right[j])
        j += 1
    
    return b2


n, m = map(int, input().split())
a = list(map(int, input().split()))

answer = []
merge(a)

if len(answer) >= m:
    print(answer[m-1])
else:
    print(-1)
