
def find_max(words):
    max_word = ""
    max_chars = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_chars or (unique_chars == max_chars and word < max_word):
            max_chars = unique_chars
            max_word = word

    return max_word

# Test cases
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))   # Output: "aaaaaaa"
