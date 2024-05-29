
def is_haiku(syllables, words):
    haiku_syllables = [5, 7, 5]
    idx = 0
    for i in range(3):
        phrase_syllables = sum(len(word) for word in words[idx:])
        if phrase_syllables != haiku_syllables[i]:
            return "come back next year"
        idx += phrase_syllables
    return "haiku"

# Read inputs
syllables = int(input())
syllable_list = input().split()
poem = [input().split() for _ in range(3)]

# Flatten the poem into words
words = [word for line in poem for word in line]

# Check if the poem is a haiku
result = is_haiku(syllables, words)
print(result)
```
