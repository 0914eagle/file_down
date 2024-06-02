
class Solution:
    def words_in_sentence(self, sentence):
        words = sentence.split(' ')
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        res = []
        for word in words:
            if len(word) in prime:
                res.append(word)
        return ' '.join(res)
