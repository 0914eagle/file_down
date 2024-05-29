
def find_max(words):
    def count_unique_chars(word):
        return len(set(word))

    max_unique = 0
    max_word = ""

    for word in words:
        unique_chars = count_unique_chars(word)
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique:
            max_word = min(max_word, word)

    return max_word

# Test cases
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))   # Output: "aaaaaaa"
