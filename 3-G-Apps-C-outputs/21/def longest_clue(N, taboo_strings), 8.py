
def longest_clue(N, taboo_strings):
    taboo_set = set(taboo_strings)
    
    def is_valid_clue(clue):
        for taboo in taboo_set:
            if taboo in clue:
                return False
        return True
    
    max_length = 0
    longest_clue = ""
    
    for i in range(1, 2**len(taboo_strings)):
        binary_string = bin(i)[2:]
        clue = binary_string.zfill(len(taboo_strings))
        
        if is_valid_clue(clue):
            if len(clue) > max_length:
                max_length = len(clue)
                longest_clue = clue
            elif len(clue) == max_length and clue < longest_clue:
                longest_clue = clue
    
    if max_length == 0:
        return -1
    else:
        return longest_clue

# Input
N = int(input())
taboo_strings = [input() for _ in range(N)]

# Output
result = longest_clue(N, taboo_strings)
print(result)
