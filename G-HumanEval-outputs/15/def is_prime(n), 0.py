
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)
    
# Test cases
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
```
