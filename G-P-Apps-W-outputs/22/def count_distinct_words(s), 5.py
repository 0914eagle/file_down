
def count_distinct_words(s):
    n = len(s)
    distinct_words = set()
    for i in range(n):
        shifted = s[-i:] + s[:-i]
        distinct_words.add(shifted)
    return len(distinct_words)

# Read input
s = input().strip()

# Calculate and print the result
result = count_distinct_words(s)
print(result)
```
