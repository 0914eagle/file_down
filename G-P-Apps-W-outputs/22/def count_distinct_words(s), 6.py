
def count_distinct_words(s):
    n = len(s)
    unique_words = set()
    
    for i in range(n):
        new_word = s[-i:] + s[:-i]
        unique_words.add(new_word)
    
    return len(unique_words)

# Read input
s = input().strip()

# Calculate and print the number of distinct words
print(count_distinct_words(s))
```
