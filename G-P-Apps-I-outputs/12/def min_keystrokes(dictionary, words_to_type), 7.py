
def min_keystrokes(dictionary, words_to_type):
    keystrokes = []
    for word in words_to_type:
        min_keystroke = float('inf')
        for i in range(len(word)):
            prefix = word[:i+1]
            for dict_word in dictionary:
                if dict_word.startswith(prefix):
                    keystroke = len(prefix) + 1 + len(word) - len(prefix)
                    min_keystroke = min(min_keystroke, keystroke)
                    break
        keystrokes.append(min_keystroke)
    return keystrokes

# Input parsing
n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]
words_to_type = [input() for _ in range(m)]

# Calculate minimum keystrokes
result = min_keystrokes(dictionary, words_to_type)

# Output
for res in result:
    print(res)

# Test the function with the provided example
dictionary_example = ['austria', 'autocorrect', 'program', 'programming', 'computer']
words_to_type_example = ['autocorrelation', 'programming', 'competition', 'zyx', 'austria']
result_example = min_keystrokes(dictionary_example, words_to_type_example)
for res in result_example:
    print(res)
```
