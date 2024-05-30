
def count_words_with_pattern(words, pattern):
    count = 0
    for word in words:
        if len(word) == len(pattern) - 1 and all(word[i] == pattern[i] or pattern[i] == '*' for i in range(len(word))):
            count += 1
    return count

# Input
N, Q = map(int, input().split())
words = [input().strip() for _ in range(N)]
patterns = [input().strip() for _ in range(Q)]

# Output
for pattern in patterns:
    print(count_words_with_pattern(words, pattern))
```
