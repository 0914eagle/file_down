
from itertools import permutations

def count_test_sentences(N, words):
    all_letters = set("abcdefghijklmnopqrstuvwxyz")
    possible_sentences = set()
    
    for perm in permutations(words):
        sentence = "".join(perm)
        if set(sentence) == all_letters:
            possible_sentences.add(sentence)
    
    return len(possible_sentences)

# Read input
N = int(input())
words = [input().strip() for _ in range(N)]

# Call the function and output the result
result = count_test_sentences(N, words)
print(result)
```
