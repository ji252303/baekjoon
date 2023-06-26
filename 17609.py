def check(str,left,right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def samecheck(str, left, right):
    if str == str[::-1]:
        return 0
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            leftcheck = check(str, left + 1, right)
            rightcheck = check(str, left, right - 1)
            if leftcheck or rightcheck:
                return 1
            else:
                return 2

t = int(input())

for i in range(t):
    str = input()
    print(samecheck(str, 0 , len(str)-1))
