
def max_teams(t, test_cases):
    for test_case in test_cases:
        n = test_case[0]
        weights = test_case[1]

        weight_count = {}
        for w in weights:
            if w in weight_count:
                weight_count[w] += 1
            else:
                weight_count[w] = 1

        max_teams = 0
        for s in range(2, 2 * n + 1):
            teams = 0
            for weight, count in weight_count.items():
                if s - weight in weight_count:
                    teams += min(count, weight_count[s-weight])
            max_teams = max(max_teams, teams // 2)

        print(max_teams)

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

max_teams(t, test_cases)
