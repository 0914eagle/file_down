
def mex(s):
    i = 0
    while True:
        if i not in s:
            return i
        i += 1

def max_team_strength(n, m, potentials, clubs, d, leave_days):
    clubs_dict = {}
    for i in range(n):
        if clubs[i] not in clubs_dict:
            clubs_dict[clubs[i]] = []
        clubs_dict[clubs[i]].append(potentials[i])

    for day in range(d):
        leave_student = leave_days[day]
        clubs_dict[clubs[leave_student - 1]].remove(potentials[leave_student - 1])

        max_strength = 0
        for club in clubs_dict.values():
            if club:
                max_strength = max(max_strength, mex(club))

        print(max_strength)

# Input parsing
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leave_days = [int(input()) for _ in range(d)]

max_team_strength(n, m, potentials, clubs, d, leave_days)
