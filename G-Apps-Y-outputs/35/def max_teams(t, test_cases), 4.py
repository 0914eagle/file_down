
def max_teams(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        weights = test_cases[i][1]
        
        weight_count = {}
        for w in weights:
            if w in weight_count:
                weight_count[w] += 1
            else:
                weight_count[w] = 1
        
        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for w in weight_count:
                if s - w in weight_count:
                    teams += min(weight_count[w], weight_count[s - w])
            max_teams = max(max_teams, teams // 2)
        
        results.append(max_teams)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

# Solve the problem
output = max_teams(t, test_cases)

# Output
for result in output:
    print(result)
