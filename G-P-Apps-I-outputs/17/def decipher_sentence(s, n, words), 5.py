
def decipher_sentence(s, n, words):
    def is_valid(s):
        return any(s == word or (s[0] == word[0] and s[-1] == word[-1] and sorted(s[1:-1]) == sorted(word[1:-1])) for word in words)

    def decipher_word(word):
        for w in words:
            if word == w or (word[0] == w[0] and word[-1] == w[-1] and sorted(word[1:-1]) == sorted(w[1:-1])):
                return w
        return None

    def find_deciphered_sentence(s, start):
        if start == len(s):
            return []
        for i in range(start, len(s)):
            word = s[start:i+1]
            if is_valid(word):
                rest = find_deciphered_sentence(s, i+1)
                if rest is not None:
                    return [decipher_word(word)] + rest
        return None

    deciphered = find_deciphered_sentence(s, 0)
    if deciphered is None:
        return "impossible"
    elif any(c.isalpha() for c in s):
        return "ambiguous"
    else:
        return ' '.join(deciphered)


# Read input
s = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

# Call the function and print the output
print(decipher_sentence(s, n, words))
```
