import sys
n= int(sys.stdin.readline())

stack =[]

for _ in range (n):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        stack.append(word[1])

    if word[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    if word[0] == 'size':
        print(len(stack))

    if word[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    if word[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
