
def is_haiku(syllables, words):
    syllable_dict = {}
    for syllable in syllables:
        syllable_dict[syllable] = syllable_dict.get(syllable, 0) + 1

    haiku_lines = [[], [], []]
    haiku_counts = [5, 7, 5]

    for line_num, line in enumerate(words):
        curr_count = 0
        curr_syllable = ""
        for word in line.split():
            word_len = len(word)
            for i in range(word_len):
                curr_syllable += word[i]
                if curr_syllable in syllable_dict:
                    curr_count += 1
                    syllable_dict[curr_syllable] -= 1
                    if syllable_dict[curr_syllable] == 0:
                        del syllable_dict[curr_syllable]
                    curr_syllable = ""
            if curr_count > haiku_counts[line_num]:
                return "come back next year"
            elif curr_count == haiku_counts[line_num]:
                haiku_lines[line_num].append(" ".join(line.split()[:word_len-i]))

    if len(syllable_dict) > 0 or len(haiku_lines[0]) != 1 or len(haiku_lines[1]) != 1 or len(haiku_lines[2]) != 1:
        return "come back next year"
    return "haiku"

# Read input
syllable_count = int(input())
syllables = input().split()
words = [input() for _ in range(3)]

# Check if poem is a haiku
result = is_haiku(syllables, words)
print(result)
```
