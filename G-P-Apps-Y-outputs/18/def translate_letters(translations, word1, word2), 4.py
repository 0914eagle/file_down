
def translate_letters(translations, word1, word2):
    if len(word1) != len(word2):
        return "no"
    
    translation_dict = dict(translations)
    
    for i in range(len(word1)):
        if word1[i] in translation_dict:
            if translation_dict[word1[i]] != word2[i]:
                return "no"
        elif word1[i] != word2[i]:
            return "no"
    
    return "yes"

# Input
m, n = map(int, input().split())
translations = [input().split() for _ in range(m)]
word_pairs = [input().split() for _ in range(n)]

# Output
for pair in word_pairs:
    print(translate_letters(translations, pair[0], pair[1]))
```
