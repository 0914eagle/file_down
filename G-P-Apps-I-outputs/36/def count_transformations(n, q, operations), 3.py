
def count_transformations(n, q, operations):
    def dfs(s):
        if len(s) == 1:
            return int(s == 'a')
        
        count = 0
        for a, b in operations:
            if s.startswith(a):
                new_s = s.replace(a, b, 1)
                count += dfs(new_s)
        
        return count
    
    count = 0
    for i in range(6 ** n):
        s = ''.join([chr(ord('a') + (i // 6 ** j) % 6) for j in range(n)])
        count += dfs(s)
    
    return count

# Input
n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

# Output
print(count_transformations(n, q, operations))
```
