
def max_square_length(k, test_cases):
    results = []
    for i in range(k):
        n = test_cases[i][0]
        planks = test_cases[i][1]
        planks.sort(reverse=True)
        max_length = 0
        for j in range(n):
            max_length = max(max_length, min(j + 1, planks[j]))
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
output = max_square_length(k, test_cases)
for result in output:
    print(result)
