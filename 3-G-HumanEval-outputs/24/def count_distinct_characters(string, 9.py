
def count_distinct_characters(string: str) -> int:
    return len(set(char.lower() for char in string))

print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
