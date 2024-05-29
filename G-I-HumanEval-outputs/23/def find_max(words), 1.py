
def find_max(words):
    max_unique_chars = 0
    result = ""
    
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < result):
            max_unique_chars = unique_chars
            result = word
    
    return result

# Test cases
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # Output: "aaaaaaa"
