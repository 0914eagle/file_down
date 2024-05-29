
def score_words(words):
    score = 0
    vowels = "aeiouy"

    for word in words:
        vowel_count = sum(1 for letter in word if letter in vowels)
        if vowel_count % 2 == 0:
            score += 2
        else:
            score += 1

    return score

# Read input
n = int(input())
words = input().split()

# Call the function and print the output
print(score_words(words))
```
