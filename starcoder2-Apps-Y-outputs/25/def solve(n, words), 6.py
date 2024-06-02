
def solve(n, words):
    words_set = set()
    for word in words:
        if word in words_set:
            return "No"
        if len(words_set) > 0 and word[0] != words[-1][-1]:
            return "No"
        words_set.add(word)
    return "Yes"

n = int(input())
words = [input() for _ in range(n)]
print(solve(n, words))

