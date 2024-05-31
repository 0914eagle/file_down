
def max_square(k, test_cases):
    results = []
    for i in range(k):
        n = test_cases[i][0]
        planks = test_cases[i][1]

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
output = max_square(k, test_cases)
for result in output:
    print(result)
