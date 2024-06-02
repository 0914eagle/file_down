
def shiritori(words):
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0] or words[i] == words[i+1]:
            return "No"
    return "Yes"

n = int(input())
words = []
for i in range(n):
    words.append(input())

print(shiritori(words))

