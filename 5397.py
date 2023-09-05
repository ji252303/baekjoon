import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    tmp = input().rstrip()
    pwd = []
    sub = []
    for a in tmp:
        if a == '<':
            if pwd:
                sub.append(pwd.pop())
        elif a == '>':  
            if sub:
                pwd.append(sub.pop())
        elif a == '-':
            if pwd:
                pwd.pop()
        else:
            pwd.append(a)  # 위의 3가지 문자 외 어느 문자든 전부 pwd에 삽입
    print("".join(pwd), "".join(sub[::-1]), sep="")
