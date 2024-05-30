
def distinct_words_count(s):
    s = s.strip()
    n = len(s)
    distinct_words = set()
    
    for i in range(n):
        shifted_word = s[-i:] + s[:-i]
        distinct_words.add(shifted_word)
    
    return len(distinct_words)

# Take input
s = input().strip()

# Output the result
print(distinct_words_count(s))
```
