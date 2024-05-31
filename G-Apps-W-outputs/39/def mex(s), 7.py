
def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def max_team_strength(n, m, potentials, clubs, d, leaving_students):
    club_to_students = [[] for _ in range(m)]
    for i in range(n):
        club_to_students[clubs[i] - 1].append(potentials[i])

    team_strengths = []
    for i in range(d):
        leaving_student = leaving_students[i] - 1
        club_of_leaving_student = clubs[leaving_student]
        club_to_students[club_of_leaving_student - 1].remove(potentials[leaving_student])

        team_potentials = []
        for j in range(m):
            if club_to_students[j]:
                team_potentials.append(max(club_to_students[j]))

        team_strengths.append(mex(set(team_potentials)))

    return team_strengths

# Input
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leaving_students = [int(input()) for _ in range(d)]

# Output
result = max_team_strength(n, m, potentials, clubs, d, leaving_students)
for strength in result:
    print(strength)
