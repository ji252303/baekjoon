import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))

if max(visit) == 0 :
    print("SAD")
else:
    visit_num = sum(visit[0:x])
    value = visit_num
    count = 1

    for i in range(x, n):
        value -= visit[i-x]
        value += visit[i]
        if value > visit_num:
            visit_num = value
            count = 1
        elif value == visit_num:
            count += 1
        
    print(visit_num)
    print(count)
