
def longest_clue(N, taboo_strings):
    taboo_set = set(taboo_strings)
    taboo_set_len = len(taboo_set)
    
    def is_valid(clue):
        for taboo in taboo_set:
            if taboo in clue:
                return False
        return True
    
    if all(len(taboo) == 1 for taboo in taboo_set):
        return '1' * taboo_set_len
    
    max_length = 0
    max_clue = ''
    
    for i in range(1, 2 ** taboo_set_len):
        clue = bin(i)[2:].zfill(taboo_set_len)
        if is_valid(clue):
            if len(clue) > max_length:
                max_length = len(clue)
                max_clue = clue
            elif len(clue) == max_length and clue < max_clue:
                max_clue = clue
    
    if max_length == 0:
        return -1
    return max_clue

# Input parsing
N = int(input())
taboo_strings = [input().strip() for _ in range(N)]

# Call the function and print the output
print(longest_clue(N, taboo_strings))
