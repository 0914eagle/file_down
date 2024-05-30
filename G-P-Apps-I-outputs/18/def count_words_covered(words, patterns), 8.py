
def count_words_covered(words, patterns):
    def is_covered(word, pattern):
        if len(word) != len(pattern):
            return False
        for i in range(len(word)):
            if pattern[i] != "*" and pattern[i] != word[i]:
                return False
        return True

    word_counts = []
    for pattern in patterns:
        count = 0
        for word in words:
            if is_covered(word, pattern):
                count += 1
        word_counts.append(count)
    return word_counts

# Input parsing
N, Q = map(int, input().split())
words = [input().strip() for _ in range(N)]
patterns = [input().strip() for _ in range(Q)]

# Count words covered by each pattern
result = count_words_covered(words, patterns)

# Output the results
for count in result:
    print(count)
```
