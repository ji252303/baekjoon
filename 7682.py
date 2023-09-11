import sys
input = sys.stdin.readline

def solve():
    while True:
        case = input().strip()
        if case == 'end':
            break
        x_count = case.count('X')
        o_count = case.count('O')

        if x_count == o_count + 1 or x_count == o_count:
            tp1,tp2 = ('X','O') if x_count == o_count+1 else ('O','X')
            result1 = check_game_end(case,tp1)
            result2 = check_game_end(case,tp2)

            if result2:
                print('invalid')
            elif not result1:
                if case.count('.') == 0:
                    print('valid')
                else:
                    print('invalid')
            else:
                print('valid')
        else:
            print('invalid')




def check_game_end(case,typ):
    if case[0] == typ and case[0] == case[1] == case[2]:
        return True
    elif case[0] == typ and case[0] == case[3] == case[6]:
        return True
    elif case[4] == typ and case[1] == case[4] == case[7]:
        return True
    elif case[4] == typ and case[3] == case[4] == case[5]:
        return True
    elif case[8] == typ and case[6] == case[7] == case[8]:
        return True
    elif case[8] == typ and case[2] == case[5] == case[8]:
        return True
    elif case[4] == typ and case[0] == case[4] == case[8]:
        return True
    elif case[4] == typ and case[2] == case[4] == case[6]:
        return True
    else:
        return False

solve()
