
def shiritori(n, words):
    for i in range(1, n):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            return "No"
    return "Yes"

n = int(input())
words = [input() for _ in range(n)]
print(shiritori(n, words))

