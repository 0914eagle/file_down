
def maximum_team_strength(n, m, potentials, club_indices, d, leaving_students):
    clubs = [[] for _ in range(m)]
    for i in range(n):
        clubs[club_indices[i] - 1].append(potentials[i])

    mex = lambda s: next(i for i in range(len(s)+2) if i not in s)

    for i in range(d):
        leaving_student = leaving_students[i] - 1
        club_of_leaving_student = club_indices[leaving_student] - 1
        clubs[club_of_leaving_student].remove(potentials[leaving_student])

        team_strengths = []
        for j in range(m):
            if clubs[j]:
                team_strengths.append(mex(clubs[j]))

        print(max(team_strengths))

n, m = map(int, input().split())
potentials = list(map(int, input().split()))
club_indices = list(map(int, input().split()))
d = int(input())
leaving_students = [int(input()) for _ in range(d)]

maximum_team_strength(n, m, potentials, club_indices, d, leaving_students)
