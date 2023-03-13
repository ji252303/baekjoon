while True:
    a= input()


    if a == '.':
        break

    stack = []
    n = True

    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                n = False
                break
            elif stack[-1] == '[':
                stack.pop()
        elif i == ')':
            if len(stack) == 0 or stack[-1] == '[':
                n = False
                break
            elif stack[-1] == '(':
                stack.pop()

    if len(stack) == 0 and n == True:
        print("yes")
    else:
        print("no")
