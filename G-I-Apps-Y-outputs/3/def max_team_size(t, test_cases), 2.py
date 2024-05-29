
def max_team_size(t, test_cases):
    res = []
    
    for _ in range(t):
        n = test_cases[_][0]
        skills = test_cases[_][1]
        
        freq = {}
        for skill in skills:
            freq[skill] = freq.get(skill, 0) + 1
        
        max_size = max(min(len(set(skills)), freq[skill]) for skill in freq)
        res.append(max_size)
    
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
for res in result:
    print(res)
