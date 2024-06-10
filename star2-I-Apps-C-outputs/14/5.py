
def rhymes(word1, word2):
    min_len = min(len(word1), len(word2))
    for i in range(min_len, max(min_len - 3, 0), -1):
        if word1[-i:] == word2[-i:]:
            return True
    return False


def check_consistency(statements):
    equivalent_words = {}
    for statement in statements:
        word1, word2 = statement.split(" is ")
        if word1 not in equivalent_words:
            equivalent_words[word1] = set()
        equivalent_words[word1].add(word2)
        if word2 not in equivalent_words:
            equivalent_words[word2] = set()
        equivalent_words[word2].add(word1)
    for word1, equivalent_set in equivalent_words.items():
        for word2 in equivalent_set:
            if word1 != word2 and not rhymes(word1, word2):
                return "wait what?"

    return "yes"

statements = [
    "herp is derp",
    "derp is herp",
    "herp is herp",
    "derp is derp"
]

print(check_consistency(statements))

