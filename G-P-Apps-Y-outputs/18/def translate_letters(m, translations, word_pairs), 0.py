
def translate_letters(m, translations, word_pairs):
    translation_dict = {translation[0]: translation[1] for translation in translations}

    def translate_word(word):
        translated_word = ''
        for letter in word:
            translated_word += translation_dict.get(letter, letter)
        return translated_word

    for pair in word_pairs:
        word1, word2 = pair
        if len(word1) != len(word2):
            print("no")
        else:
            translated_word1 = translate_word(word1)
            translated_word2 = translate_word(word2)
            if translated_word1 == translated_word2:
                print("yes")
            else:
                print("no")

# Read input
m, n = map(int, input().split())
translations = [input().split() for _ in range(m)]
word_pairs = [input().split() for _ in range(n)]

# Call the function
translate_letters(m, translations, word_pairs)
```
