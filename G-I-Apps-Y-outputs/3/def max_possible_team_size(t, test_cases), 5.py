
def max_possible_team_size(t, test_cases):
    res = []
    for case in test_cases:
        n = case[0]
        skills = case[1]

        freq = {}
        unique_skills = set()
        for skill in skills:
            freq[skill] = freq.get(skill, 0) + 1
            unique_skills.add(skill)

        max_size = min(len(unique_skills), max(freq.values()))
        res.append(max_size)

    return res


# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))
    test_cases.append((n, skills))

# Get the results
results = max_possible_team_size(t, test_cases)

# Output
for res in results:
    print(res)
```
