
def max_teams(t, test_cases):
    res = []
    
    for i in range(t):
        n = test_cases[i][0]
        weights = test_cases[i][1]

        weight_count = {}
        for weight in weights:
            weight_count[weight] = weight_count.get(weight, 0) + 1

        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for weight in weight_count:
                if weight * 2 <= s:
                    teams += min(weight_count[weight], weight_count.get(s - weight, 0))
            max_teams = max(max_teams, teams // 2)

        res.append(max_teams)

    return res

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

# Output
output = max_teams(t, test_cases)
for ans in output:
    print(ans)
