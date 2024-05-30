
def create_translation_dict(translations):
    translation_dict = {}
    for translation in translations:
        translation_dict[translation[0]] = translation[1]
    return translation_dict

def apply_translation(translation_dict, word):
    translated_word = ''
    for letter in word:
        if letter in translation_dict:
            translated_word += translation_dict[letter]
        else:
            translated_word += letter
    return translated_word

def check_word_match(original_word, deciphered_word):
    if len(original_word) != len(deciphered_word):
        return False
    for i in range(len(original_word)):
        if original_word[i] != deciphered_word[i]:
            return False
    return True

m, n = map(int, input().split())
translations = [input().split() for _ in range(m)]
word_pairs = [input().split() for _ in range(n)]

translation_dict = create_translation_dict(translations)

for pair in word_pairs:
    original_word = pair[0]
    deciphered_word = pair[1]

    translated_original_word = apply_translation(translation_dict, original_word)
    
    if check_word_match(translated_original_word, deciphered_word):
        print("yes")
    else:
        print("no")
```
