n = input()
if 'x' in n:
    pos = n.find('x')
    if pos == 0:
        print(1)
    elif pos == 1 and n[0] == '-':
        print(-1)
    else:
        print(int(n[:pos]))
else:
    print(0)
