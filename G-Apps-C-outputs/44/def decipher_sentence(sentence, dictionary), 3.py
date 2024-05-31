
def decipher_sentence(sentence, dictionary):
    sentence = list(sentence)
    n = len(sentence)
    valid_words = set(dictionary)

    # Helper function to check if a word is valid
    def is_valid_word(w):
        return w in valid_words

    # Helper function to check if a word can be formed from a given section of the sentence
    def is_valid_word_from_section(start, end):
        word = ''.join(sentence[start:end])
        return is_valid_word(word)

    # Initialize list to store possible word boundaries
    word_boundaries = [0]
    for i in range(1, n):
        if is_valid_word_from_section(word_boundaries[-1], i):
            word_boundaries.append(i)

    # Check if last character is a word boundary
    if word_boundaries[-1] != n:
        if is_valid_word_from_section(word_boundaries[-1], n):
            word_boundaries.append(n)
        else:
            return "impossible"

    # Construct and return deciphered sentence
    deciphered_sentence = ' '.join(''.join(sentence[word_boundaries[i]:word_boundaries[i+1]]) for i in range(len(word_boundaries) - 1))
    return deciphered_sentence

# Read input
sentence = input().strip()
n = int(input().strip())
dictionary = [input().strip() for _ in range(n)]

# Call the function to decipher the sentence
result = decipher_sentence(sentence, dictionary)
print(result if result else "ambiguous")
