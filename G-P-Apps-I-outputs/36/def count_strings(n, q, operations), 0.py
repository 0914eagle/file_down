
def count_strings(n, q, operations):
    count = 0
    for i in range(6 ** n):
        s = ''
        for j in range(n):
            s += chr(ord('a') + (i // 6 ** (n-j-1)) % 6)
        
        can_transform = True
        while len(s) > 1 and can_transform:
            found = False
            for a, b in operations:
                if s.startswith(a):
                    s = b + s[2:]
                    found = True
                    break
            if not found:
                can_transform = False
        
        if len(s) == 1 and s == 'a':
            count += 1
    
    return count

# Input parsing
n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

# Call the function and print the output
print(count_strings(n, q, operations))
```
