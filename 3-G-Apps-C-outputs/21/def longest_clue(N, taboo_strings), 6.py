
def longest_clue(N, taboo_strings):
    taboo_set = set(taboo_strings)
    max_length = 0
    longest_clue = ""

    def is_valid_clue(clue):
        for taboo in taboo_set:
            if taboo in clue:
                return False
        return True

    def generate_clues(clue):
        nonlocal max_length, longest_clue
        if len(clue) > max_length and is_valid_clue(clue):
            max_length = len(clue)
            longest_clue = clue
        elif len(clue) == max_length and is_valid_clue(clue):
            longest_clue = min(longest_clue, clue)

        if len(clue) < max_length:
            for bit in ['0', '1']:
                generate_clues(clue + bit)

    generate_clues("")
    
    if max_length == 0:
        return -1
    else:
        return longest_clue

# Input parsing
N = int(input())
taboo_strings = [input().strip() for _ in range(N)]

result = longest_clue(N, taboo_strings)
print(result)
