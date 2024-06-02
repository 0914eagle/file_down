
def longest_clue(N, taboo_strings):
    taboo_set = set(taboo_strings)
    max_length = 0
    longest_clue = ""

    def is_valid_clue(clue):
        for taboo in taboo_set:
            if taboo in clue:
                return False
        return True

    def generate_clues(clue, length):
        nonlocal max_length, longest_clue
        if length > max_length:
            if is_valid_clue(clue):
                max_length = length
                longest_clue = clue
            for i in ["0", "1"]:
                generate_clues(clue + i, length + 1)

    generate_clues("", 0)

    if max_length == 0:
        return -1
    else:
        return longest_clue

# Read input
N = int(input())
taboo_strings = [input().strip() for _ in range(N)]

# Call the function and print the result
result = longest_clue(N, taboo_strings)
print(result)
