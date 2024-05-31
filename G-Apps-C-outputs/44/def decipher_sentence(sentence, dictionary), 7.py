
def decipher_sentence(sentence, dictionary):
    def is_valid_decipher(deciphered):
        words = deciphered.split()
        for word in words:
            if word not in dictionary:
                return False
        return True

    def decipher_helper(text, deciphered):
        if not text:
            if is_valid_decipher(deciphered):
                return [deciphered]
            else:
                return []

        results = []
        for i in range(1, len(text) + 1):
            new_deciphered = deciphered + text[:i] + " "
            remaining_text = text[i:]
            sub_results = decipher_helper(remaining_text, new_deciphered)
            results.extend(sub_results)

        return results

    results = decipher_helper(sentence, "")
    
    if not results:
        return "impossible"
    elif len(results) > 1:
        return "ambiguous"
    else:
        return results[0]

# Input parsing
sentence = input().strip()
n = int(input())
dictionary = set()
for _ in range(n):
    word = input().strip()
    dictionary.add(word)

output = decipher_sentence(sentence, dictionary)
print(output)
