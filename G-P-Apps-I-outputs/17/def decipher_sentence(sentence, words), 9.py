
def decipher_sentence(sentence, words):
    def is_valid(word):
        return word in words
    
    def is_decipherable(word):
        return len(word) == 1 or (is_valid(word[0]) and is_valid(word[-1]) and all(is_valid(w) for w in word[1:-1]))
    
    def dfs(remaining):
        if not remaining:
            return []
        
        deciphered = []
        for i in range(1, len(remaining)+1):
            prefix = remaining[:i]
            suffix = remaining[i:]
            if is_decipherable(prefix):
                suffix_deciphered = dfs(suffix)
                if suffix_deciphered is not None:
                    deciphered = [prefix] + suffix_deciphered
                    break
        return deciphered if deciphered else None
    
    deciphered_sentence = dfs(sentence)
    return ' '.join(deciphered_sentence) if deciphered_sentence else 'impossible'

s = input().strip()
n = int(input())
words = set(input().strip() for _ in range(n))

result = decipher_sentence(s, words)
print(result if result else 'ambiguous')
```
