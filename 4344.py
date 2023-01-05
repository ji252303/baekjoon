case = int(input())


for i in range(case):
    n = list(map(int,input().split()))
    avg = sum(n[1:])/n[0]
    ct = 0
    for score in n[1:]:
        if score > avg:
           ct += 1
    rate = ct/n[0] * 100
    print(f'{rate:.3f}%')
