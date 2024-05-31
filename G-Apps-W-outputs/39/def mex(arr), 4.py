
def mex(arr):
    s = set(arr)
    mex_val = 0
    while mex_val in s:
        mex_val += 1
    return mex_val

def max_team_strength(n, m, potentials, clubs, d, leave_days):
    club_members = [[] for _ in range(m)]
    team_strengths = []

    for i in range(n):
        club_members[clubs[i]-1].append(potentials[i])

    for leave_day in leave_days:
        club_idx = clubs[leave_day-1] - 1
        club_members[club_idx].remove(potentials[leave_day-1])

        max_team_strength = 0
        for club in club_members:
            if club:
                max_team_strength = max(max_team_strength, mex(club))
        
        team_strengths.append(max_team_strength)
    
    return team_strengths

# Input parsing
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leave_days = [int(input()) for _ in range(d)]

# Get maximum team strength for each day
result = max_team_strength(n, m, potentials, clubs, d, leave_days)

# Output the results
for strength in result:
    print(strength)
