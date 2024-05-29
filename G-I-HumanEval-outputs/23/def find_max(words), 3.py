
def find_max(words):
    def count_unique_chars(word):
        return len(set(word))

    unique_chars_map = {word: count_unique_chars(word) for word in words}
    max_unique_chars = max(unique_chars_map.values())
    
    candidates = [word for word, count in unique_chars_map.items() if count == max_unique_chars]
    return min(candidates)

# Test cases
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))   # Output: "aaaaaaa"
