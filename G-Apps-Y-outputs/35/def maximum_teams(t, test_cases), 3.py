
def maximum_teams(t, test_cases):
    results = []
    
    for _ in range(t):
        n = test_cases[_][0]
        weights = test_cases[_][1]
        weights_count = {}
        
        for weight in weights:
            if weight not in weights_count:
                weights_count[weight] = 1
            else:
                weights_count[weight] += 1
        
        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for weight in weights_count:
                if s - weight in weights_count:
                    teams += min(weights_count[weight], weights_count[s - weight])
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

# Get maximum teams for each test case
output = maximum_teams(t, test_cases)

# Output the results
for result in output:
    print(result)
