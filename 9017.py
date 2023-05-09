import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    members = list(map(lambda x: int(x), input().split()))

    team_members = defaultdict(int)
    for member in members:
        team_members[member] += 1

    score = 1
    # score, count, 5_member_score, team
    teams = [[0, 0, 0, i] for i in range(len(team_members) + 1)]
    for member in members:
        if team_members[member] < 6:
            teams[member] = [1001, 1001, 1001, 0]
            continue
        if teams[member][1] < 4:
            teams[member][0] += score
            teams[member][1] += 1
        elif teams[member][1] == 4:
            teams[member][2] = score
            teams[member][1] += 1
        score += 1

    teams.sort(key=lambda x: (x[0], x[2]))
    print(teams[1][3])
