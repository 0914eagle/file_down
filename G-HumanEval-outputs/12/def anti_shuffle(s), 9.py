
def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        result.append(sorted_word)
    return ' '.join(result)

# Test cases
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'ehllo !!!Wdlor'
