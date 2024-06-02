
def words_in_sentence(sentence):
    words = sentence.split()
    return ' '.join(word for word in words if len(word) in primes)
 