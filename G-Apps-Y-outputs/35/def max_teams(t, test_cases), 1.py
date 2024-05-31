
def max_teams(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        weights = test_cases[i][1]

        count_dict = {}
        for weight in weights:
            if weight in count_dict:
                count_dict[weight] += 1
            else:
                count_dict[weight] = 1

        max_teams = 0
        for s in range(2, 2*n+1):
            teams = 0
            for weight in count_dict:
                partner_weight = s - weight
                if partner_weight in count_dict and count_dict[partner_weight] > 0:
                    min_pairs = min(count_dict[weight], count_dict[partner_weight])
                    teams += min_pairs
                    count_dict[weight] -= min_pairs
                    count_dict[partner_weight] -= min_pairs

            max_teams = max(max_teams, teams)

        print(max_teams)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    test_cases.append((n, weights))

max_teams(t, test_cases)
