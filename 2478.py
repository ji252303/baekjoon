import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# res : (뒤집는 시작점, 뒤집는 끝점, 두번째 왼쪽밀기의 정도)
res = []
for i in range(n - 1, 0, -1):
    # temp : 두번째 왼쪽밀기를 원래대로 되돌린 수열
    temp = arr[i : n] + arr[ : i]
    # cnt : 뒤집기가 가능한 크기
    cnt = 0
    start = -1
    for j in range(n - 1):
        # 현재 수가 1이 아니라면 1, 현재 수가 1이라면 n - 1의 차이가 나는 경우만 가능
        if (temp[j] - 1 > 0 and temp[j + 1] == temp[j] - 1) or (temp[j] - 1 == 0 and temp[j + 1] == n):
            cnt += 1
            # 시작점 갱신
            if start == -1:
                start = j
    # 뒤집기가 가능하면 저장
    if cnt > 0:
        res.append((start, cnt, i))

res.sort(key=lambda x : (-(x[1] - x[0])))
arr = arr[res[0][2] : n] + arr[:res[0][2]] # 두번째 왼쪽 밀기 이전으로 되돌림
arr = arr[:res[0][0]] + arr[res[0][0] : res[0][1] + 1][::-1] + arr[res[0][1] + 1 : n] # 뒤집기 이전으로 되돌림
idx = arr.index(1) # idx : 처음 왼쪽 밀기를 한 후 1의 인덱스

print(n-idx)
print(res[0][0]+1, res[0][1] + 1)
print(n - res[0][2])

정답오류가 있음?? 후에 한번 더풀때 참고
