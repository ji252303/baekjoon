import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
word = list(input().split())
word.sort()
comb = list(combinations(word, L))
vowel = ['a', 'e', 'i', 'o', 'u']

for i in comb:
    ja = 0
    mo = 0
    answer = ''
    for j in i:
        if j in vowel:
            mo += 1
        else:
            ja += 1
        answer += j
    if mo >= 1 and ja >= 2:
        print(answer)
