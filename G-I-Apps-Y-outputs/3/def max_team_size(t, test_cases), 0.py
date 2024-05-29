
def max_team_size(t, test_cases):
    result = []
    
    for i in range(t):
        n = test_cases[i][0]
        skills = test_cases[i][1]
        skill_count = {}
        unique_skills = set()
        
        for skill in skills:
            if skill in skill_count:
                skill_count[skill] += 1
            else:
                skill_count[skill] = 1
                unique_skills.add(skill)
        
        max_size = min(len(unique_skills), max(skill_count.values()))
        result.append(max_size)
    
    return result


# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))
    test_cases.append((n, skills))

# Solve the problem for each test case
output = max_team_size(t, test_cases)

# Output the results
for res in output:
    print(res)
```
