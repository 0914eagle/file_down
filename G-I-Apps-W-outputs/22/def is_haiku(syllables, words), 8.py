
def is_haiku(syllables, words):
    haiku = [5, 7, 5]
    index = 0
    
    for line in words:
        count = 0
        split_line = line.split()
        
        for word in split_line:
            count += len(word)
            
            if count == syllables[index]:
                count = 0
                index += 1
            elif count > syllables[index]:
                return "come back next year"
        
        if count != 0:
            return "come back next year"
    
    return "haiku"

# Read input values
syllables = list(map(int, input().strip().split()))
poem = [input() for _ in range(3)]

# Calculate the number of syllables for each word in the poem
syllable_counts = [sum(len(word) for word in line.split()) for line in poem]

# Check if the given poem is a haiku
result = is_haiku(syllables, poem)
print(result)
