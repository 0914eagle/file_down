
def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def max_team_strength(n, m, potentials, clubs, d, leave_days):
    students = [[] for _ in range(m)]
    for i in range(n):
        students[clubs[i]-1].append(potentials[i])
    
    team_strengths = []
    for day in range(d):
        leaving_student = leave_days[day] - 1
        club_idx = clubs[leaving_student] - 1
        students[club_idx].remove(potentials[leaving_student])
        
        team_potentials = [max(student) if student else 0 for student in students]
        team_strengths.append(mex(set(team_potentials)))
    
    return team_strengths

# Input reading
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leave_days = [int(input()) for _ in range(d)]

# Calculate and print output
output = max_team_strength(n, m, potentials, clubs, d, leave_days)
for strength in output:
    print(strength)
