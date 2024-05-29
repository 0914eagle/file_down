
def score_words(words):
    score = 0
    vowels = 'aeiouy'

    for word in words:
        num_vowels = 0
        for letter in word:
            if letter in vowels:
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
``` 

