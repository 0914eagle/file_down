
def max_team_size(t, test_cases):
    result = []
    
    for test_case in test_cases:
        n = test_case[0]
        skills = test_case[1]
        
        unique_skills = len(set(skills))
        max_same_skill = max(skills.count(skill) for skill in set(skills))
        
        max_size = min(unique_skills, max_same_skill)
        result.append(max_size)
    
    return result

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))
    test_cases.append((n, skills))

# Call the function
output = max_team_size(t, test_cases)

# Output the results
for x in output:
    print(x)
