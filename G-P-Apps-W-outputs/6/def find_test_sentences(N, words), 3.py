
from itertools import permutations

def find_test_sentences(N, words):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    possible_sentences = set()
    
    for perm in permutations(words):
        sentence = ' '.join(perm)
        if alphabet.issubset(sentence):
            possible_sentences.add(sentence)
    
    return len(possible_sentences)

# Reading input
N = int(input())
words = [input() for _ in range(N)]

# Output
print(find_test_sentences(N, words))
```
