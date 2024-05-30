
def count_transformations(n, q, operations):
    def dfs(s):
        if len(s) == 1:
            return 1
        count = 0
        for ai, bi in operations:
            if s.startswith(ai):
                count += dfs(bi + s[2:])
        return count

    count = 0
    for i in range(6**n):
        s = "".join([chr(ord('a') + i // 6**j % 6) for j in range(n)])
        count += dfs(s)
    
    return count

# Input parsing
n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

# Call the function with input values
result = count_transformations(n, q, operations)
print(result)
```
