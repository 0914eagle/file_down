
def max_possible_team_size(t, test_cases):
    for case in test_cases:
        n = case[0]
        skills = case[1]

        skill_counts = {}
        for skill in skills:
            if skill not in skill_counts:
                skill_counts[skill] = 1
            else:
                skill_counts[skill] += 1

        max_team_size = min(len(set(skills)), max(skill_counts.values()))
        print(max_team_size)

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))
    test_cases.append((n, skills))

max_possible_team_size(t, test_cases)
```
