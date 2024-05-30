
def decipher_words(m, n, translations, word_pairs):
    translation_dict = dict(translations)
    
    def can_translate(word1, word2):
        if len(word1) != len(word2):
            return False
        
        for i in range(len(word1)):
            if word1[i] not in translation_dict:
                if word1[i] != word2[i]:
                    return False
            else:
                if translation_dict[word1[i]] != word2[i]:
                    return False
        
        return True
    
    results = []
    for pair in word_pairs:
        if can_translate(pair[0], pair[1]):
            results.append("yes")
        else:
            results.append("no")
    
    return results

# Input parsing
m, n = map(int, input().split())
translations = [input().split() for _ in range(m)]
word_pairs = [input().split() for _ in range(n)]

# Call the function with the provided inputs
output = decipher_words(m, n, translations, word_pairs)

# Output the results
for result in output:
    print(result)
