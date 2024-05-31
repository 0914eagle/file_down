
def decipher_sentence(s, words):
    n = len(s)
    possible_words = []

    for word in words:
        if len(word) == n:
            if word[0] == s[0] and word[-1] == s[-1]:
                possible_words.append(word)

    if not possible_words:
        return "impossible"
    
    result = ""
    for word in possible_words:
        mapping = {s[i]: word[i] for i in range(1, n-1)}
        deciphered = word[0] + ''.join(mapping[char] for char in s[1:-1]) + word[-1]
        
        if deciphered == s:
            return word
    
    return "ambiguous"

# Input
s = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Output
print(decipher_sentence(s, words))
