
def find_max_team_size(t, test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        skills = case[1]
        
        unique_skills = set()
        same_skills = {}
        
        for skill in skills:
            if skill not in unique_skills:
                unique_skills.add(skill)
            if skill not in same_skills:
                same_skills[skill] = 1
            else:
                same_skills[skill] += 1
        
        max_size = max(min(len(unique_skills), sum(same_skills.values())), 0)
        results.append(max_size)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))
    test_cases.append((n, skills))

# Call the function with the inputs
output = find_max_team_size(t, test_cases)

# Output the results
for result in output:
    print(result)
