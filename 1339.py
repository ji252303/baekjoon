n = int(input())
words = []
alpha_dict = {}
for _ in range(n):
    words.append(input())

for word in words:
    root = len(word) - 1
    for i in word:
        if i in alpha_dict:
            alpha_dict[i] += pow(10, root)
        else:
            alpha_dict[i] = pow(10, root)

        root -= 1

alpha_dict = sorted(alpha_dict.values(), reverse=True)

result, m = 0, 9

for value in alpha_dict:
    result += value * m
    m -= 1

print(result)
