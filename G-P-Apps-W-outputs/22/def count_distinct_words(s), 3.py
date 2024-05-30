
def count_distinct_words(s):
    n = len(s)
    words = set()
    for i in range(n):
        rotated_word = s[-i:] + s[:-i]
        words.add(rotated_word)
    return len(words)

# Input
s = input().strip()

# Output
print(count_distinct_words(s))
```
