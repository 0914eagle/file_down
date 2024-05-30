
def count_possible_strings(n, q, operations):
    def helper(s):
        if len(s) == 1 and s == 'a':
            return 1
        count = 0
        for a, b in operations:
            if s.startswith(a):
                new_s = s.replace(a, b, 1)
                count += helper(new_s)
        return count

    count = 0
    for i in range(6 ** n):
        s = ''.join([chr((i // 6**j) % 6 + ord('a')) for j in range(n)])
        count += helper(s)
    
    return count

# Input parsing
n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

# Calculate and print the output
print(count_possible_strings(n, q, operations))
```
