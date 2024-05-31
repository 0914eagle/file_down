
def max_teams(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        weights = test_cases[i][1]
        
        weight_count = {}
        for weight in weights:
            if weight in weight_count:
                weight_count[weight] += 1
            else:
                weight_count[weight] = 1
        
        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for weight in weight_count.keys():
                if s - weight in weight_count:
                    teams += min(weight_count[weight], weight_count[s - weight])
            max_teams = max(max_teams, teams // 2)
        
        results.append(max_teams)
    
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

# Output
output = max_teams(t, test_cases)
for res in output:
    print(res)
