
def count_distinct_strings(s):
    unique_strings = set()
    for i in range(len(s)):
        shifted_string = s[-i:] + s[:-i]
        unique_strings.add(shifted_string)
    return len(unique_strings)

# Input
s = input().strip()

# Output
print(count_distinct_strings(s))
```
