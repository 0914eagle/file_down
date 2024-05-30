
def min_keystrokes(dictionary, words_to_type):
    result = []
    prefix_freq = {}
    for word in dictionary:
        for i in range(1, len(word)+1):
            prefix = word[:i]
            if prefix not in prefix_freq:
                prefix_freq[prefix] = len(prefix) + 1  # pressing tab and len(prefix) backspaces
    for word_to_type in words_to_type:
        min_keystrokes = len(word_to_type)  # typing the whole word without using autocorrect
        for i in range(1, len(word_to_type) + 1):
            prefix = word_to_type[:i]
            if prefix in prefix_freq:
                keystrokes = prefix_freq[prefix] + len(word_to_type[i:])
                min_keystrokes = min(min_keystrokes, keystrokes)
        result.append(min_keystrokes)
    return result

# Input processing
n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]
words_to_type = [input() for _ in range(m)]

# Output
output = min_keystrokes(dictionary, words_to_type)
for keystrokes in output:
    print(keystrokes)
```
