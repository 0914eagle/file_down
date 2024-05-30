
def count_distinct_words(s):
    n = len(s)
    distinct_words = set()
    
    for i in range(n):
        new_word = s[-i:] + s[:-i]
        distinct_words.add(new_word)
    
    return len(distinct_words)

# Input
s = input().strip()

# Output
print(count_distinct_words(s))
```
