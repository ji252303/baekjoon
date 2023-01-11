case = int(input())
n = case
for i in range(case):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            n -= 1
            break

print(n)
