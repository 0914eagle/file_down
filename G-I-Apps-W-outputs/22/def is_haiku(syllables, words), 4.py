
def is_haiku(syllables, words):
    haiku = [words[:5], words[5:12], words[12:]]
    syllable_idx = 0
    for line in haiku:
        line_syllables = []
        for word in line:
            word_syllables = []
            while len(word) > 0:
                for i in range(1, min(8, len(word)+1)):
                    if word[:i] in syllables:
                        word_syllables.append(word[:i])
                        word = word[i:]
                        break
            line_syllables.extend(word_syllables)
        if len(line_syllables) != 5:
            return "come back next year"
    
    return "haiku"

# Input parsing
syllable_count = int(input())
syllables = input().split()
poem = [input().split() for _ in range(3)]

result = is_haiku(syllables, [word for line in poem for word in line])
print(result)
```
