
def longest_clue(N, taboo_strings):
    taboo_set = set(taboo_strings)
    
    def is_valid_clue(clue):
        for taboo in taboo_set:
            if taboo in clue:
                return False
        return True
    
    max_length = 0
    longest_clue = ""
    
    for i in range(1, 2**len(taboo_strings[0])):
        binary_clue = format(i, 'b')
        if is_valid_clue(binary_clue):
            if len(binary_clue) > max_length:
                max_length = len(binary_clue)
                longest_clue = binary_clue
            elif len(binary_clue) == max_length and binary_clue < longest_clue:
                longest_clue = binary_clue
    
    if max_length == 0:
        return -1
    else:
        return longest_clue

# Input parsing
N = int(input())
taboo_strings = [input().strip() for _ in range(N)]

result = longest_clue(N, taboo_strings)
print(result)
