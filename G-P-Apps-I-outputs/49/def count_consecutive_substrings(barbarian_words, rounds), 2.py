
def count_consecutive_substrings(barbarian_words, rounds):
    all_words = set()
    word_count = {}
    
    for word in barbarian_words:
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                all_words.add(word[i:j])
    
    for word in all_words:
        word_count[word] = 0
    
    result = []
    for t, query in rounds:
        if t == 1:
            for i in range(len(query)):
                for j in range(i+1, len(query)+1):
                    all_words.add(query[i:j])
        elif t == 2:
            count = 0
            for word in barbarian_words[query-1]:
                count += word_count[word]
            result.append(count)
    
    return result

# Read input
N = int(input())
barbarian_words = [input().strip() for _ in range(N)]
Q = int(input())
rounds = []
for _ in range(Q):
    t, *rest = input().split()
    t = int(t)
    if t == 1:
        p = rest[0]
        rounds.append((t, p))
    elif t == 2:
        s = int(rest[0])
        rounds.append((t, s))

# Call the function
output = count_consecutive_substrings(barbarian_words, rounds)

# Print output
for count in output:
    print(count)
```
