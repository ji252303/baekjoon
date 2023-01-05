n = int(input())

for i in range(n):
    a = list(input())
    score = 0
    sum = 1
    for i in a:
        if i == 'O':
            score += sum
            sum += 1
        else:
            sum = 1
    print(score)
