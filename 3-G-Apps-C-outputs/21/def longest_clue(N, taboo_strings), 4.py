
def longest_clue(N, taboo_strings):
    taboo_strings.sort(key=len, reverse=True)
    
    def is_valid_clue(clue, taboo_strings):
        for taboo in taboo_strings:
            if taboo in clue:
                return False
        return True
    
    max_length = sum(len(taboo) for taboo in taboo_strings) + 1
    longest_clue = -1
    
    for length in range(max_length):
        for clue in itertools.product('01', repeat=length):
            clue_str = ''.join(clue)
            if is_valid_clue(clue_str, taboo_strings):
                longest_clue = max(longest_clue, clue_str)
    
    return longest_clue

# Input parsing
N = int(input())
taboo_strings = [input().strip() for _ in range(N)]

result = longest_clue(N, taboo_strings)
print(result)
