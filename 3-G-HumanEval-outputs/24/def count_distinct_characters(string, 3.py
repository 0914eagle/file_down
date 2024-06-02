
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
