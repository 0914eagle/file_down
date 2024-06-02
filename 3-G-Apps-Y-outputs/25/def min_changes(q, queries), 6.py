
def min_changes(q, queries):
    def count_changes(s, k):
        min_changes = float('inf')
        for i in range(len(s) - k + 1):
            changes = sum(s[i+j] != 'RGB'[j % 3] for j in range(k))
            min_changes = min(min_changes, changes)
        return min_changes

    results = []
    for query in queries:
        n, k, s = query
        result = count_changes(s, k)
        results.append(result)

    return results

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n, k = map(int, input().split())
    s = input().strip()
    queries.append((n, k, s))

# Call the function and print the results
results = min_changes(q, queries)
for result in results:
    print(result)
