
def decipher_sentence(s, n, words):
    def is_valid(word, s_part):
        if len(word) != len(s_part):
            return False
        if word[0] != s_part[0] or word[-1] != s_part[-1]:
            return False
        sorted_word = sorted(word[1:-1])
        sorted_s_part = sorted(s_part[1:-1])
        return sorted_word == sorted_s_part

    possibilities = []
    for word in words:
        if is_valid(word, s):
            possibilities.append(word)

    if not possibilities:
        return "impossible"
    elif len(possibilities) == 1:
        return possibilities[0]
    else:
        return "ambiguous"

# Read input
s = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

# Output
result = decipher_sentence(s, n, words)
print(result)
