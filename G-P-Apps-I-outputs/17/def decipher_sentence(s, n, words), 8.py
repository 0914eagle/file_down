
def decipher_sentence(s, n, words):
    def is_valid_word(word):
        return any(word in w for w in words)

    def shuffle_word(word):
        return word[0] + ''.join(sorted(word[1:-1])) + word[-1]

    def decipher(s):
        words = s.split()
        result = []
        for word in words:
            shuffled_word = shuffle_word(word)
            if is_valid_word(shuffled_word):
                result.append(shuffled_word)
            else:
                return "impossible"
        return " ".join(result)

    if len(s) == sum(len(word) for word in words) + n - 1:
        return decipher(s)
    else:
        return "ambiguous"

# Read input
s = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

# Output result
result = decipher_sentence(s, n, words)
print(result)
```
