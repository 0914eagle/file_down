
def mex(arr):
    i = 0
    while i in arr:
        i += 1
    return i

def max_team_strength(n, m, potentials, clubs, d, leaving_students):
    club_members = {}
    for i in range(1, m+1):
        club_members[i] = []
    for i in range(n):
        club_members[clubs[i]].append(potentials[i])
    
    team_strengths = []
    for day in range(d):
        student = leaving_students[day]
        club = clubs[student-1]
        club_members[club].remove(potentials[student-1])
        
        strengths = []
        for key, value in club_members.items():
            if len(value) > 0:
                strengths.append(max(value))
        
        team_strengths.append(mex(strengths))
    
    return team_strengths

# Input
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leaving_students = [int(input()) for _ in range(d)]

# Output
results = max_team_strength(n, m, potentials, clubs, d, leaving_students)
for result in results:
    print(result)
