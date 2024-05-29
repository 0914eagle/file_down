
def is_haiku(syllables, words):
    haiku_syllables = [5, 7, 5]
    haiku_phrases = []
    current_syllable = 0

    for word in words:
        for i in range(1, len(word)):
            if word[:i] in syllables:
                haiku_phrases.append(word[:i])
                current_syllable += len(word[:i])
                syllables.remove(word[:i])
                break

    if haiku_phrases == []:
        return "come back next year"

    for syllable_count in haiku_syllables:
        if current_syllable < syllable_count:
            return "come back next year"
        current_syllable -= syllable_count

    return "haiku"

# Read input
n_syllables = int(input())
syllables = input().split()
poem = [input().split() for _ in range(3)]

# Check if the poem is a haiku
result = is_haiku(syllables, sum(poem, []))
print(result)
