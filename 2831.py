from bisect import bisect_left

def match(small, bigger):
    global res
    smallst= 0
    biggerst = len(bigger) - 1

    while smallst < len(small) and biggerst >= 0:
        if small[smallst] + bigger[biggerst] < 0:
            res += 1
            smallst += 1
            biggerst -= 1
        else:
            biggerst -=1

n = int(input())
men = sorted((list(map(int, input().split()))))
women = sorted((list(map(int, input().split()))))
res = 0

men_p = bisect_left(men, 0)
women_p = bisect_left(women, 0)

match(men[:men_p], women[women_p:])
match(women[:women_p], men[men_p:])

print(res)
