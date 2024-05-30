
def count_distinct_words(s):
    n = len(s)
    distinct_words = set()

    for i in range(n):
        shifted_word = s[-i:] + s[:-i]
        distinct_words.add(shifted_word)

    return len(distinct_words)

# Input
s = input().strip()

# Output
result = count_distinct_words(s)
print(result)
```
