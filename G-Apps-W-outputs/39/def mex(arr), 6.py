
def mex(arr):
    s = set(arr)
    mex_val = 0
    while mex_val in s:
        mex_val += 1
    return mex_val

def maximum_team_strength(n, m, potentials, clubs, days, leaving_students):
    club_members = [[] for _ in range(m)]
    for i in range(n):
        club_members[clubs[i] - 1].append(potentials[i])

    team_strengths = []
    for day in range(days):
        leaving_student = leaving_students[day] - 1
        club_of_leaving_student = clubs[leaving_student] - 1
        club_members[club_of_leaving_student].remove(potentials[leaving_student])

        max_strength = 0
        for club in club_members:
            if club:
                max_strength = max(max_strength, mex(club))

        team_strengths.append(max_strength)

    return team_strengths

# Input
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
days = int(input())
leaving_students = [int(input()) for _ in range(days)]

# Output
result = maximum_team_strength(n, m, potentials, clubs, days, leaving_students)
for strength in result:
    print(strength)
