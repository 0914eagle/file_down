
def decipher_sentence(s, n, dictionary):
    def is_valid_decipher(deciphered, words):
        words = set(words)
        split = deciphered.split()
        for word in split:
            if word not in words:
                return False
        return True

    def decipher_word(word, first, last):
        return first + ''.join(sorted(word[1:-1])) + last

    first = s[0]
    last = s[-1]
    s = s[1:-1]
    words = []
    for word in dictionary:
        if len(word) == len(s):
            if set(word) == set(s):
                words.append(word)

    if not words:
        return "impossible"
    elif len(words) > 1:
        return "ambiguous"
    else:
        deciphered = decipher_word(words[0], first, last)
        if is_valid_decipher(deciphered, dictionary):
            return deciphered
        else:
            return "ambiguous"

# Read input
s = input().strip()
n = int(input().strip())
dictionary = [input().strip() for _ in range(n)]

# Call the function and print the output
result = decipher_sentence(s, n, dictionary)
print(result)
