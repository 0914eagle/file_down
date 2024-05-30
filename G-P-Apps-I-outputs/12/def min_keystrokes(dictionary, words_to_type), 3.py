
def min_keystrokes(dictionary, words_to_type):
    result = []
    for word in words_to_type:
        min_keystrokes = len(word)  # Initialize with the length of the word
        for i in range(1, len(word)+1):
            prefix = word[:i]
            if prefix in dictionary:
                keystrokes = len(prefix) + 1 + len(word) - len(prefix)  # keystrokes = prefix + tab + remaining characters
                min_keystrokes = min(min_keystrokes, keystrokes)
        result.append(min_keystrokes)
    return result

# Read input
n, m = map(int, input().split())
dictionary = set()
for _ in range(n):
    dictionary.add(input().strip())

words_to_type = []
for _ in range(m):
    words_to_type.append(input().strip())

# Get the minimum keystrokes required for each word
output = min_keystrokes(dictionary, words_to_type)

# Print the output
for keystrokes in output:
    print(keystrokes)

```
