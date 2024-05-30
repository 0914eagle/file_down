
def decipher_sentence(sentence, dictionary):
    def shuffle_word(word):
        return word[0] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1]
    
    def is_valid(arrangement):
        for word in arrangement.split():
            if word not in dictionary:
                return False
        return True

    words = sentence.split()
    if len(words) == 0:
        return "impossible"
    
    # Check all possible shufflings
    valid_arrangements = []
    for perm in itertools.permutations(words[1:-1]):
        shuffled_sentence = words[0] + ''.join(perm) + words[-1]
        if is_valid(shuffled_sentence):
            valid_arrangements.append(shuffled_sentence)
    
    if len(valid_arrangements) == 1:
        return valid_arrangements[0]
    elif len(valid_arrangements) > 1:
        return "ambiguous"
    else:
        return "impossible"

# Input parsing
sentence = input().strip()
n = int(input().strip())
dictionary = set()
for _ in range(n):
    word = input().strip()
    dictionary.add(word)

result = decipher_sentence(sentence, dictionary)
print(result)
```
