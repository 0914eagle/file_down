
def mex(arr):
    s = set(arr)
    mex_val = 0
    while mex_val in s:
        mex_val += 1
    return mex_val

def max_team_strength(n, m, potentials, clubs, d, leaving_students):
    teams = {}
    students_by_club = {}
    
    for i in range(n):
        club = clubs[i]
        if club not in students_by_club:
            students_by_club[club] = []
        students_by_club[club].append(potentials[i])
        
    for i in range(d):
        leaving_student = leaving_students[i]
        club = clubs[leaving_student-1]
        students_by_club[club].remove(potentials[leaving_student-1])
        
        for club, potentials in students_by_club.items():
            if len(potentials) > 0:
                team_strength = max(potentials) + 1
                teams[club] = team_strength
            else:
                teams[club] = 0
        
        print(max(teams.values()))

n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leaving_students = [int(input()) for _ in range(d)]

max_team_strength(n, m, potentials, clubs, d, leaving_students)
