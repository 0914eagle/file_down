
def anti_shuffle(s):
    words = s.split()
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)
    
    result = ' '.join(ordered_words)
    
    return result

# Test cases
print(anti_shuffle('Hi'))  # 'Hi'
print(anti_shuffle('hello'))  # 'ehllo'
print(anti_shuffle('Hello World!!!'))  # 'Hello !!!Wdlor'
