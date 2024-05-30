
def count_ways_to_transform(n, q, operations):
    def dfs(s, target, operations, idx):
        if idx == n - 1:
            return s == target
        
        count = 0
        for op in operations:
            a, b = op
            if s.startswith(a):
                count += dfs(s.replace(a, b, 1), target, operations, idx + 1)
        
        return count
    
    initial_strings = [''.join([c for c in 'abcdef' if i % 6**(5 - i) // 6**(4 - i)]) for i in range(6**n)]
    total_count = 0
    for s in initial_strings:
        total_count += dfs(s, 'a', operations, 0)
    
    return total_count

# Parse input
n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

# Call the function and print the output
print(count_ways_to_transform(n, q, operations))
```
