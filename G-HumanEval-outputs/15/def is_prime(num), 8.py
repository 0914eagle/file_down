
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    sentence_words = sentence.split()
    prime_words = [word for word in sentence_words if is_prime(len(word))]
    return ' '.join(prime_words)

# Test the function
sentence1 = "This is a test"
print(words_in_sentence(sentence1))  # Output: "is"

sentence2 = "lets go for swimming"
print(words_in_sentence(sentence2))  # Output: "go for"
