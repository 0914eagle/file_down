
# Function to solve the problem
def max_team_size(t, test_cases):
    result = []
    for i in range(t):
        n, skills = test_cases[i]

        skill_counts = {}
        for skill in skills:
            if skill in skill_counts:
                skill_counts[skill] += 1
            else:
                skill_counts[skill] = 1

        unique_skills = len(set(skills))
        max_team_size = min(unique_skills, max(skill_counts.values()))

        result.append(max_team_size)

    return result

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))
    test_cases.append((n, skills))

# Call the function and output the result
output = max_team_size(t, test_cases)
for x in output:
    print(x)
```
