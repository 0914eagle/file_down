
def count_covered_words(words, patterns):
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

# Calculate and output the result
for count in count_covered_words(words, patterns):
    print(count)
```
