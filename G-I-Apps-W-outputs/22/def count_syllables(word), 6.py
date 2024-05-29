
def count_syllables(word):
    # Dummy function to count syllables, can be implemented based on rules or a dictionary
    return len(word)

def is_haiku(syllables, lines):
    counts = [0, 0, 0]
    
    for idx, line in enumerate(lines):
        for word in line.split():
            counts[idx] += count_syllables(word)
    
    if counts == syllables:
        return "haiku"
    else:
        return "come back next year"

# Input processing
syllables_count = int(input())
syllables = list(map(int, input().strip().split()))

poem_lines = []
for _ in range(3):
    poem_lines.append(input().strip())

# Check if the poem is a haiku
result = is_haiku(syllables, poem_lines)
print(result)
```
