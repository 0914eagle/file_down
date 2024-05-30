
def count_words_covered(words, queries):
    counts = []
    for query in queries:
        count = 0
        for word in words:
            if len(query) == len(word):
                match = True
                for i in range(len(query)):
                    if query[i] != '*' and query[i] != word[i]:
                        match = False
                        break
                if match:
                    count += 1
        counts.append(count)
    return counts

# Input processing
N, Q = map(int, input().split())
words = [input() for _ in range(N)]
queries = [input() for _ in range(Q)]

# Output
for count in count_words_covered(words, queries):
    print(count)
```
