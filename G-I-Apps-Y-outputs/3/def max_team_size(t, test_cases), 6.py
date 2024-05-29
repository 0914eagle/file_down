
def max_team_size(t, test_cases):
    res = []
    for i in range(t):
        n = test_cases[i][0]
        skills = test_cases[i][1]

        skill_counts = {}
        same_skill = 0
        unique_skills = set()

        for skill in skills:
            if skill in skill_counts:
                skill_counts[skill] += 1
                same_skill = max(same_skill, skill_counts[skill])
            else:
                skill_counts[skill] = 1
                unique_skills.add(skill)

        if len(unique_skills) >= same_skill:
            res.append(min(len(unique_skills), same_skill))
        else:
            res.append((len(unique_skills) + same_skill)//2)

    return res

# Input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))
    test_cases.append((n, skills))

# Output
result = max_team_size(t, test_cases)
for r in result:
    print(r)
