
def remaining_number(n, x):
    if x == 1:
        return 1
    return 2 * x

# Input processing
T = int(input())
queries = []
for _ in range(T):
    n, x = map(int, input().split())
    queries.append((n, x))

# Solve queries
results = []
for n, x in queries:
    results.append(remaining_number(n, x))

# Output results
for result in results:
    print(result)
