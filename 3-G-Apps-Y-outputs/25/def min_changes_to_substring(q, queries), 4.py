
def min_changes_to_substring(q, queries):
    def count_changes(s, k):
        min_changes = float('inf')
        for i in range(len(s) - k + 1):
            changes = sum(1 for j in range(k) if s[i + j] != "RGB"[j % 3])
            min_changes = min(min_changes, changes)
        return min_changes

    results = []
    for query in queries:
        n, k, s = query
        changes = count_changes(s, k)
        results.append(changes)

    return results

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n, k = map(int, input().split())
    s = input().strip()
    queries.append((n, k, s))

# Call the function and print results
results = min_changes_to_substring(q, queries)
for result in results:
    print(result)
