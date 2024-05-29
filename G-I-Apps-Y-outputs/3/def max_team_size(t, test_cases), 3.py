
def max_team_size(t, test_cases):
    result = []
    
    for test_case in test_cases:
        n = test_case[0]
        skills = test_case[1]
        
        skill_count = {}
        for skill in skills:
            if skill not in skill_count:
                skill_count[skill] = 0
            skill_count[skill] += 1
        
        max_size = 0
        for count in skill_count.values():
            max_size = max(max_size, min(count, n - count))
        
        result.append(max_size)
    
    return result

# Input
t = 4
test_cases = [
    (7, [4, 2, 4, 1, 4, 3, 4]),
    (5, [2, 1, 5, 4, 3]),
    (1, [1]),
    (4, [1, 1, 1, 3])
]

# Output
output = max_team_size(t, test_cases)
for o in output:
    print(o)
