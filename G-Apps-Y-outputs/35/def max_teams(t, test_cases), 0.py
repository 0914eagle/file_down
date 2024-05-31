
def max_teams(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        weights = test_cases[i][1]

        freq = {}
        for w in weights:
            freq[w] = freq.get(w, 0) + 1
        
        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for w in freq:
                if s - w in freq:
                    teams += min(freq[w], freq[s - w])
            max_teams = max(max_teams, teams // 2)
        
        results.append(max_teams)
    
    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

# Call the function
output = max_teams(t, test_cases)

# Output
for k in output:
    print(k)
