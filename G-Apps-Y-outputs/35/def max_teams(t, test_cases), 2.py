
def max_teams(t, test_cases):
    res = []
    
    for i in range(t):
        n = test_cases[i][0]
        weights = test_cases[i][1]

        freq = {}
        for w in weights:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1

        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for w in freq:
                if w <= s//2 and s-w in freq:
                    teams += min(freq[w], freq[s-w])
            max_teams = max(max_teams, teams//2)

        res.append(max_teams)

    return res


# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

# Call the function with input data and print the output
output = max_teams(t, test_cases)
for ans in output:
    print(ans)
