
# Define a Python function to solve the problem
def remaining_number(T, queries):
    results = []
    for n, x in queries:
        remaining = x
        for i in range(x+1, n+1):
            remaining = 2 * remaining
            if remaining >= i:
                break
        results.append(remaining)
    return results

# Read input
T = int(input())
queries = []
for _ in range(T):
    n, x = map(int, input().split())
    queries.append((n, x))

# Call the function and print the output
output = remaining_number(T, queries)
for result in output:
    print(result)
