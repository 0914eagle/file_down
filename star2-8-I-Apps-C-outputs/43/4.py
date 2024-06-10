
def findLongestAlternatingSubsequence(scores):
    current_length = 1
    max_length = 1
    for i in range(1, len(scores)):
        if scores[i] != scores[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    max_length = max(max_length, current_length)
    return max_length

n = int(input())
scores = input()
result = findLongestAlternatingSubsequence(scores)
print(result)

