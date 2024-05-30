
def translate_letters(translations, word1, word2):
    if len(word1) != len(word2):
        return "no"
    
    mapping = {}
    for a, b in translations:
        mapping[a] = b
    
    for i in range(len(word1)):
        if word1[i] not in mapping:
            if word1[i] != word2[i]:
                return "no"
        elif mapping[word1[i]] != word2[i]:
            return "no"
    
    return "yes"

# Read input
m, n = map(int, input().split())
translations = [input().split() for _ in range(m)]
word_pairs = [input().split() for _ in range(n)]

# Check word pairs
for pair in word_pairs:
    result = translate_letters(translations, pair[0], pair[1])
    print(result)
