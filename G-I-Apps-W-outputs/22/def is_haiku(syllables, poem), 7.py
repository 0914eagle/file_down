
def is_haiku(syllables, poem):
    syl_dict = {}
    for syllable in syllables:
        syl_dict[syllable] = syl_dict.get(syllable, 0) + 1

    lines = [poem[:poem.index(" ")], poem[poem.index(" ") + 1:poem.rindex(" ")], poem[poem.rindex(" ") + 1:]]
    line_syl = []
    for line in lines:
        line_syl_count = 0
        words = line.split()
        for word in words:
            word_syls = []
            start = 0
            for i in range(1, len(word) + 1):
                if word[start:i] in syl_dict:
                    word_syls.append(word[start:i])
                    start = i
            if len(word_syls) == 0:
                return "come back next year"
            line_syl_count += len(word_syls)
        line_syl.append(line_syl_count)

    if line_syl == [5, 7, 5]:
        return "haiku"
    else:
        return "come back next year"

# Input
syllables = int(input())
syllable_words = input().split()
poem = input() + " " + input() + " " + input()

# Output
print(is_haiku(syllable_words, poem))
```
