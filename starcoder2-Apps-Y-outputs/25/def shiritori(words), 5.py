
def shiritori(words):
    if len(words) < 2:
        return 'Yes'
    for i in range(1, len(words)):
        if words[i] == words[i-1] or words[i][0] != words[i-1][-1]:
            return 'No'
    return 'Yes'

n = int(input())
words = [input() for _ in range(n)]
print(shiritori(words))

