
def is_haiku(syllables, words):
    syllables_dict = {}
    for s in syllables:
        if len(s) not in syllables_dict:
            syllables_dict[len(s)] = [s]
        else:
            syllables_dict[len(s)].append(s)

    haiku = []
    for line in words:
        line_syllables = []
        word = ''
        for char in line:
            word += char
            if len(word) in syllables_dict:
                if word in syllables_dict[len(word)]:
                    line_syllables.append(word)
                    word = ''
        haiku.append(line_syllables)

    if len(haiku[0]) == 5 and len(haiku[1]) == 7 and len(haiku[2]) == 5:
        return "haiku"
    else:
        return "come back next year"

# Read input
syllable_count = int(input())
syllables = input().split()
poem_lines = [input().split() for _ in range(3)]

# Check if poem is a haiku
result = is_haiku(syllables, ' '.join(poem_lines).split())
print(result)
```
