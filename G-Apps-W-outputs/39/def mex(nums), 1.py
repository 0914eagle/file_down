
def mex(nums):
    nums = set(nums)
    i = 0
    while i in nums:
        i += 1
    return i

def team_strength(n, m, potentials, clubs, d, leave_days):
    club_to_students = [[] for _ in range(m)]
    for i in range(n):
        club_to_students[clubs[i] - 1].append(potentials[i])

    team_strengths = []
    for day in range(d):
        student_idx = leave_days[day] - 1
        club_idx = clubs[student_idx] - 1
        club_to_students[club_idx].remove(potentials[student_idx])

        team_potentials = []
        for club in club_to_students:
            if club:
                team_potentials.append(max(club))
        team_strengths.append(mex(team_potentials))

    return team_strengths

# Input parsing
n, m = map(int, input().split())
potentials = list(map(int, input().split()))
clubs = list(map(int, input().split()))
d = int(input())
leave_days = [int(input()) for _ in range(d)]

# Calculate and print team strengths
result = team_strength(n, m, potentials, clubs, d, leave_days)
for strength in result:
    print(strength)
