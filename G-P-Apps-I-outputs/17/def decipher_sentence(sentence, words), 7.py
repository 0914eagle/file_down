
def decipher_sentence(sentence, words):
    def is_valid(word):
        return word in words

    def decipher_recursive(s):
        if not s:
            return []
        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[i:]
            if is_valid(prefix) and deciphered_suffix := decipher_recursive(suffix):
                return [prefix] + deciphered_suffix
        if is_valid(s):
            return [s]
        return None

    deciphered = decipher_recursive(sentence)
    if deciphered:
        return ' '.join(deciphered)
    else:
        return "impossible"

# Read input
sentence = input().strip()
n = int(input())
dictionary = set(input().strip() for _ in range(n))

# Output
print(decipher_sentence(sentence, dictionary))
```
