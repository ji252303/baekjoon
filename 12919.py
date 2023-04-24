import sys
input = sys.stdin.readline

def check(n):
    global flag

    if len(n) == len(s):
        if n == s:
            flag = True
        return


    if n[-1] == 'A':
        n.pop()
        check(n)
        n.append('A')

    if n[0] == 'B':
        n.reverse()
        n.pop()
        check(n)
        n.append('B')
        n.reverse()


s = list(map(str, input().strip()))
t = list(map(str, input().strip()))
flag = False
check(t)

if flag:
    print(1)
else:
    print(0)
