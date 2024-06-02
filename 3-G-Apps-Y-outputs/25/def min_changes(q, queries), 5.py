
def min_changes(q, queries):
    result = []
    
    for query in queries:
        n, k = query[0], query[1]
        s = query[2]
        
        min_changes = float('inf')
        for i in range(n - k + 1):
            substring = s[i:i+k]
            rgb_pattern = 'RGB' * (k // 3 + 1)
            changes = sum(1 for j in range(k) if substring[j] != rgb_pattern[j])
            min_changes = min(min_changes, changes)
        
        result.append(min_changes)
    
    return result

# Input
q = 3
queries = [(5, 2, 'BGGGG'), (5, 3, 'RBRGR'), (5, 5, 'BBBRR')]

# Output
output = min_changes(q, queries)
for res in output:
    print(res)
