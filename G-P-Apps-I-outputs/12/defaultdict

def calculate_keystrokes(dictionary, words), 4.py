
from collections import defaultdict

def calculate_keystrokes(dictionary, words):
    word_dict = defaultdict(int)
    for idx, word in enumerate(dictionary):
        for i in range(1, len(word) + 1):
            word_dict[word[:i]] = max(word_dict[word[:i]], len(word) - i)
    
    for word in words:
        keystrokes = 0
        i = 0
        while i < len(word):
            prefix = word[:i + 1]
            if prefix in word_dict:
                keystrokes += 1
                keystrokes += word_dict[prefix]
                i += len(word_dict[prefix])
            else:
                keystrokes += 1
                i += 1
        print(keystrokes)

# Read input
n, m = map(int, input().split())
dictionary = [input().strip() for _ in range(n)]
words = [input().strip() for _ in range(m)]

# Calculate and output keystrokes
calculate_keystrokes(dictionary, words)
