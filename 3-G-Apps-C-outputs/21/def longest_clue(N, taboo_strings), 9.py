
def longest_clue(N, taboo_strings):
    taboo_set = set(taboo_strings)
    longest = -1
    longest_str = ""

    def is_valid(clue):
        for taboo in taboo_set:
            if taboo in clue:
                return False
        return True

    def generate_clues(clue, length):
        nonlocal longest, longest_str
        if length > longest:
            if is_valid(clue):
                longest = length
                longest_str = clue
            for i in ["0", "1"]:
                generate_clues(clue + i, length + 1)

    generate_clues("", 0)
    return longest_str

# Read input
N = int(input())
taboo_strings = [input().strip() for _ in range(N)]

# Call the function and print the output
print(longest_clue(N, taboo_strings))
