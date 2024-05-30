
def count_initial_strings(n, q, operations):
    def dfs(s):
        if len(s) == 1:
            return 1
        res = 0
        for a, b in operations:
            if s.startswith(a):
                res += dfs(b + s[len(a):])
        return res

    count = 0
    for i in range(6**n):
        s = ''
        for j in range(n):
            s += chr(ord('a') + (i // (6**j)) % 6)
        count += dfs(s)
    
    return count

# Input
n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

# Output
print(count_initial_strings(n, q, operations))
```
