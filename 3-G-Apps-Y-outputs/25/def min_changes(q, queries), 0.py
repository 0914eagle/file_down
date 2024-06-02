
def min_changes(q, queries):
    for query in queries:
        n, k = query[0], query[1]
        s = query[2]
        
        min_changes = float('inf')
        for i in range(n - k + 1):
            substring = s[i:i+k]
            target = 'RGB' * (k // 3 + 1)
            changes = sum([1 for j in range(k) if substring[j] != target[j]])
            min_changes = min(min_changes, changes)
        
        print(min_changes)

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n, k = map(int, input().split())
    s = input().strip()
    queries.append((n, k, s))

# Call the function
min_changes(q, queries)
