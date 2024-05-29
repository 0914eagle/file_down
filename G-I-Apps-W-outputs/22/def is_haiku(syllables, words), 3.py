
def is_haiku(syllables, words):
    syl_dict = {}
    for syllable in syllables:
        syl_dict.setdefault(len(syllable), []).append(syllable)
    
    line_syllables = []
    for line in words:
        line_syl = []
        for word in line:
            for syllable_length in range(1, len(word)+1):
                if syllable_length in syl_dict:
                    for syllable in syl_dict[syllable_length]:
                        if word.startswith(syllable):
                            line_syl.append(syllable)
                            word = word[len(syllable):]
                            if word == "":
                                break
                    if word == "":
                        break
        line_syllables.append(line_syl)

    syllable_counts = [sum(len(syl) for syl in line) for line in line_syllables]
    
    if syllable_counts == [5, 7, 5]:
        return "haiku"
    else:
        return "come back next year"

# Read input
syllable_count = int(input())
syllables = input().split()
word_lines = [input().split() for _ in range(3)]

# Check if poem is a haiku
result = is_haiku(syllables, word_lines)
print(result)
```
