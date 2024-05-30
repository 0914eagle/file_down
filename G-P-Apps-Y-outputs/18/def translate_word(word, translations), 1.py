
def translate_word(word, translations):
    translation_dict = {t[0]: t[1] for t in translations}
    translated_word = ''
    for letter in word:
        if letter in translation_dict:
            translated_word += translation_dict[letter]
        else:
            translated_word += letter
    return translated_word

def words_match(word1, word2, translations):
    return len(word1) == len(word2) and translate_word(word1, translations) == word2

m, n = map(int, input().split())
translations = [input().split() for _ in range(m)]

for _ in range(n):
    pair = input().split()
    if words_match(pair[0], pair[1], translations):
        print("yes")
    else:
        print("no")
```
