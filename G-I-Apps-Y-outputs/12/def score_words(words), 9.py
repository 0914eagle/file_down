
def score_words(words):
    vowels = 'aeiouy'
    score = 0
    for word in words:
        vowel_count = sum(1 for letter in word if letter in vowels)
        if vowel_count % 2 == 0:
            score += 2
        else:
            score += 1
    return score

# Input reading code
n = int(input())
words = input().split()
print(score_words(words))
```

This function correctly calculates the score for a list of lowercase words based on the given rules. The input reading code is also included to read the input as specified in the problem statement.

You can test this function with the provided test cases using the locked template code. Let me know if you need any further assistance. 

