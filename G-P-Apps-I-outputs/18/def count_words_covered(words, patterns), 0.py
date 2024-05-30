
def count_words_covered(words, patterns):
    results = []
    for pattern in patterns:
        count = 0
        for word in words:
            if len(pattern) == len(word):
                match = True
                for i in range(len(pattern)):
                    if pattern[i] != '*' and pattern[i] != word[i]:
                        match = False
                        break
                if match:
                    count += 1
        results.append(count)
    return results

# Input
N, Q = map(int, input().split())
words = [input().strip() for _ in range(N)]
patterns = [input().strip() for _ in range(Q)]

# Output
results = count_words_covered(words, patterns)
for result in results:
    print(result)
```
