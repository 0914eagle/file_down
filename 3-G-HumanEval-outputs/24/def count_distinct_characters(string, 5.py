
def count_distinct_characters(string: str) -> int:
    string = string.lower()
    distinct_chars = set(string)
    return len(distinct_chars)

print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
