
def count_matching_words(N, Q, words, patterns):
    result = []
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
        result.append(count)
    return result

# Reading input
N, Q = map(int, input().split())
words = [input() for _ in range(N)]
patterns = [input() for _ in range(Q)]

# Counting matching words for each pattern
output = count_matching_words(N, Q, words, patterns)

# Output results
for count in output:
    print(count)
```
