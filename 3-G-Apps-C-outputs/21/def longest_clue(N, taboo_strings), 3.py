
def longest_clue(N, taboo_strings):
    taboo_set = set(taboo_strings)
    
    def is_valid_clue(clue):
        for taboo in taboo_set:
            if taboo in clue:
                return False
        return True
    
    def generate_clues(length):
        for i in range(2**length):
            clue = bin(i)[2:].zfill(length)
            if is_valid_clue(clue):
                yield clue
    
    max_length = max(len(taboo) for taboo in taboo_strings)
    for length in range(max_length, 200001):
        clues = list(generate_clues(length))
        if clues:
            return min(clues)
    
    return -1

# Input processing
N = int(input())
taboo_strings = [input() for _ in range(N)]

result = longest_clue(N, taboo_strings)
print(result)
