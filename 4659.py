list = ['a', 'e', 'i', 'o', 'u']

accept = ['ee', 'oo']
while True:
    a = 0
    b = 0
    password = input()
    if password == 'end':
        break
    count = 0

    for i in list:
        if i in password:
            count += 1

    if count < 1:
        print(f'<{password}> is not acceptable.')
        continue

    for i in range(len(password)-2):
        if password[i] in list and password[i+1] in list and password[i+2] in list:
           a = 1
        elif not password[i] in list and not password[i+1] in list and not password[i+2] in list:
           a = 1
    if a == 1:
        print(f'<{password}> is not acceptable.')
        continue

    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if password[i] == 'e' or password[i] == 'o':
                continue
            else:
                b = 1

    if b == 1:
        print(f'<{password}> is not acceptable.')
        continue
    print(f'<{password}> is acceptable.')
