
def find_max(words):
    def unique_chars(word):
        return len(set(word))

    max_num_unique = 0
    max_word = ""

    for word in words:
        num_unique = unique_chars(word)
        if num_unique > max_num_unique:
            max_num_unique = num_unique
            max_word = word
        elif num_unique == max_num_unique:
            max_word = min(max_word, word)

    return max_word

print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))    # Output: "aaaaaaa"
