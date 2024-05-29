
def find_max(words):
    def num_unique_chars(word):
        return len(set(word))

    max_word = ""
    max_unique_chars = 0

    for word in words:
        unique_chars = num_unique_chars(word)
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < max_word):
            max_word = word
            max_unique_chars = unique_chars

    return max_word

# Test cases
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # Output: "aaaaaaa"
