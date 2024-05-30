
def count_words_covered(words, patterns):
    counts = []
    for pattern in patterns:
        count = 0
        for word in words:
            if len(pattern) == len(word) and all(p == w or p == '*' for p, w in zip(pattern, word)):
                count += 1
        counts.append(count)
    return counts

# Read input
N, Q = map(int, input().split())
words = [input().strip() for _ in range(N)]
patterns = [input().strip() for _ in range(Q)]

# Output results
for count in count_words_covered(words, patterns):
    print(count)
```
