
def longest_clue(N, taboo_strings):
    taboo_strings.sort(key=len, reverse=True)
    
    def is_substring(s, taboo_strings):
        for taboo in taboo_strings:
            if taboo in s:
                return True
        return False
    
    def generate_clue(length, current_clue):
        if length == 0:
            if not is_substring(current_clue, taboo_strings):
                return current_clue
            return None
        
        for bit in ['0', '1']:
            new_clue = generate_clue(length - 1, current_clue + bit)
            if new_clue:
                return new_clue
        
        return None
    
    max_length = sum(len(s) for s in taboo_strings) + 1
    longest_clue = generate_clue(max_length, '')
    
    if longest_clue:
        return longest_clue
    else:
        return -1

# Input parsing
N = int(input())
taboo_strings = [input() for _ in range(N)]

# Call the function and print the result
result = longest_clue(N, taboo_strings)
print(result)
