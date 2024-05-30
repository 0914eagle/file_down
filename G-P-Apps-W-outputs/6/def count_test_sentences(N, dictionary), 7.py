
from itertools import permutations

def count_test_sentences(N, dictionary):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    all_words = ''.join(dictionary)
    count = 0
    for perm in permutations(all_words):
        sentence = ''.join(perm)
        if all(letter in sentence for letter in alphabet):
            count += 1
    return count

# Read input
N = int(input())
dictionary = [input().strip() for _ in range(N)]

# Call the function and print the result
result = count_test_sentences(N, dictionary)
print(result)
```
