
def count_distinct_characters(string: str) -> int:
    distinct_chars = set()
    for char in string.lower():
        if char.isalpha():
            distinct_chars.add(char)
    return len(distinct_chars)

print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
