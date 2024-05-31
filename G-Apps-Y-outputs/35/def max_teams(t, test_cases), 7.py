
def max_teams(t, test_cases):
    res = []
    
    for i in range(t):
        n, weights = test_cases[i]
        weight_count = {}
        for weight in weights:
            weight_count[weight] = weight_count.get(weight, 0) + 1
        
        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for weight in weight_count:
                if (s - weight) in weight_count:
                    teams += min(weight_count[weight], weight_count[s - weight])
            max_teams = max(max_teams, teams // 2)
        
        res.append(max_teams)
    
    return res

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

# Call the function and print the output
output = max_teams(t, test_cases)
for ans in output:
    print(ans)
