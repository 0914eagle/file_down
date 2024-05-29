
def count_syllables(word):
    vowels = 'aeiou'
    count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            count += 1
            if i < len(word) - 1 and word[i+1] in vowels:
                count -= 1
    return count

def is_haiku(syllables, poem):
    syllable_words = poem.split()
    line_syllables = [0, 0, 0]
    current_line = 0

    for word in syllable_words:
        syllable_count = count_syllables(word)
        line_syllables[current_line] += syllable_count
        if line_syllables[current_line] > syllables[(current_line+1)%3]:
            return "come back next year"
        elif line_syllables[current_line] == syllables[(current_line+1)%3]:
            current_line += 1

    if line_syllables[0] == syllables[0] and line_syllables[1] == syllables[1] and line_syllables[2] == syllables[2]:
        return "haiku"
    else:
        return "come back next year"

# Read input
syllable_count = int(input())
syllables = []
for _ in range(syllable_count):
    syllables.append(count_syllables(input()))

poem = ""
for _ in range(3):
    poem += input() + " "

# Check if poem is a haiku
result = is_haiku(syllables, poem)
print(result)
```
