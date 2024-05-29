
def check_id_property(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return 'No'
    return 'Yes'

# Read input
s = input().strip()
t = input().strip()

# Check if T satisfies the property
result = check_id_property(s, t)
print(result)
```
