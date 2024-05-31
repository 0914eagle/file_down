
def max_possible_square(k, test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        planks = case[1]

        max_length = min(planks)
        results.append(max_length)

    return results

# Input
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    planks = list(map(int, input().split()))
    test_cases.append((n, planks))

# Output
output = max_possible_square(k, test_cases)
for result in output:
    print(result)
