
def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def max_team_strength(n, m, potentials, clubs, d, leaving_students):
    team_strengths = []
    students_in_club = [[] for _ in range(m)]
    for i in range(n):
        students_in_club[clubs[i] - 1].append(potentials[i])

    for day in range(d):
        leaving_student = leaving_students[day] - 1
        clubs[leaving_student] = -1
        students_in_club_index = clubs[leaving_student]
        students_in_club[students_in_club_index].remove(potentials[leaving_student])

        team_potentials = [max(students_in_club[i]) if students_in_club[i] else 0 for i in range(m)]
        team_strengths.append(mex(team_potentials))

    return team_strengths

# Input
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leaving_students = [int(input()) for _ in range(d)]

# Output
team_strengths = max_team_strength(n, m, potentials, clubs, d, leaving_students)
for strength in team_strengths:
    print(strength)
