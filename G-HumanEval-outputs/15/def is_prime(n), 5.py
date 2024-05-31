
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)

# Test the function
sentence1 = "This is a test"
print(words_in_sentence(sentence1))  # Output: "is"

sentence2 = "lets go for swimming"
print(words_in_sentence(sentence2))  # Output: "go for"
