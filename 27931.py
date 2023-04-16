n = int(input())
point = sorted(map(int, input().split()))
abc = []
a_min = []
b_min = []

for i in range(n-1):
    abc.append(point[i + 1] - point[i])

for j in abc:
    if j % 2 == 0:
        a_min.append(j)
    elif (j+(j+1)) % 2 == 0:
        a_min.append(j+(j+1))
    else:
        b_min.append(j)

if not a_min and len(b_min) > 1:
    a_min.append(b_min[0]+b_min[1])

if not a_min:
    print(-1, min(b_min))
elif not b_min:
    print(min(a_min), -1)
else:
    print(min(a_min), min(b_min))

    

 


n = int(input())
coords = list(map(int, input().split()))

coords.sort() # 좌표값을 오름차순으로 정렬

min_even = float('inf') # 짝수 거리의 최솟값
min_odd = float('inf') # 홀수 거리의 최솟값

left = 0 # 왼쪽 포인터
right = 1 # 오른쪽 포인터

while left < n-1 and right <= n:
    dist = coords[right] - coords[left] # 두 점 사이의 거리
    if dist % 2 == 0:
        min_even = min(min_even, dist) # 짝수 거리의 최솟값 업데이트
    else:
        min_odd = min(min_odd, dist) # 홀수 거리의 최솟값 업데이트
    if right == n-1: # 오른쪽 포인터가 마지막 값까지 갔으면 왼쪽 포인터 증가
        left += 1
    else:
        right += 1 # 그렇지 않으면 오른쪽 포인터 증가

if min_odd != float('inf') and min_even != float('inf'): # 홀수 거리의 최솟값이 2개 이상일 때
    min_odd_list = [dist for dist in coords[left:right+1] if dist % 2 != 0]
    if len(min_odd_list) > 1:
        min_odd_list.sort()
        min_even = min(min_even, min_odd_list[0] + min_odd_list[1])

if min_even == float('inf'):
    min_even = -1 # 짝수 거리의 최솟값이 없을 때 -1 출력
if min_odd == float('inf'):
    min_odd = -1 # 홀수 거리의 최솟값이 없을 때 -1 출력

print(min_even, min_odd)





다른사람 참고코드 (공부필요)

import sys
input = sys.stdin.readline

n = int(input().rstrip())  # 점의 개수 n
dots = list(map(int, input().rstrip().split()))
dots.sort()

notodd = -1
odd = -1

for i in range(n - 1) :
    cnt = 0
    for j in range(i + 1, n) :
        d = abs(dots[i] - dots[j])

        if d % 2 == 0 :
            if notodd == -1 : notodd = d
            else :
                if d < notodd : notodd = d
                else : cnt += 1
        elif d % 2 == 1 :
            if odd == -1 : odd = d
            else :
                if d < odd : odd = d
                else : cnt += 1
        if cnt == 2 : break

print(str(notodd) + " " + str(odd))
