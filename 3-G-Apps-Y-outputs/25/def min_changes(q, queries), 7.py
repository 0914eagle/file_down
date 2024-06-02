
def min_changes(q, queries):
    result = []
    for query in queries:
        n, k = query[0], query[1]
        s = query[2]
        
        min_changes = float('inf')
        for i in range(n - k + 1):
            substring = s[i:i+k]
            changes = sum(1 for j in range(k) if substring[j] != "RGB"[j % 3])
            min_changes = min(min_changes, changes)
        
        result.append(min_changes)
    
    return result

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n, k = map(int, input().split())
    s = input().strip()
    queries.append((n, k, s))

# Call the function and print the output
output = min_changes(q, queries)
for res in output:
    print(res)
