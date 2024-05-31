
def decipher_sentence(s, n, dictionary):
    def is_valid(deciphered):
        words = deciphered.split()
        for word in words:
            if word not in dictionary:
                return False
        return True

    def backtrack(s, current_word, deciphered):
        if not s:
            if is_valid(deciphered):
                return deciphered
            else:
                return None

        for i in range(1, len(s) + 1):
            new_word = s[:i]
            if new_word in dictionary:
                result = backtrack(s[i:], new_word, deciphered + new_word + ' ')
                if result:
                    return result

        return None

    decoded_sentence = backtrack(s, '', '')
    if decoded_sentence:
        return decoded_sentence.strip()
    else:
        return 'impossible'

# Read input
s = input().strip()
n = int(input().strip())
dictionary = set()
for _ in range(n):
    word = input().strip()
    dictionary.add(word)

# Call the function to decipher the sentence
deciphered_sentence = decipher_sentence(s, n, dictionary)
if deciphered_sentence:
    print(deciphered_sentence)
else:
    print('ambiguous')
