
def count_starting_strings(n, q, operations):
    def dfs(s):
        if len(s) == 1:
            return s == 'a'
        count = 0
        for a, b in operations:
            if s[:2] == a:
                count += dfs(b + s[2:])
        return count

    count = 0
    for i in range(6 ** n):
        s = ''.join([chr(i % 6 + ord('a')) for i in range(n)])
        count += dfs(s)
    
    return count

# Input
n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

# Output
print(count_starting_strings(n, q, operations))
```
