
def count_words_covered(words, patterns):
    def covers(word, pattern):
        if len(word) != len(pattern):
            return False
        for i in range(len(word)):
            if pattern[i] != '*' and pattern[i] != word[i]:
                return False
        return True

    counts = []
    for pattern in patterns:
        count = 0
        for word in words:
            if covers(word, pattern):
                count += 1
        counts.append(count)
    
    return counts

# Input processing
N, Q = map(int, input().split())
words = [input().strip() for _ in range(N)]
patterns = [input().strip() for _ in range(Q)]

# Output
for count in count_words_covered(words, patterns):
    print(count)
```
