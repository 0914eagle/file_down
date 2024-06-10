
n = int(input())
scores = [int(x) for x in input()]
score = 0
longest = 0
current = 1
for i in range(1, n):
    if scores[i] == scores[i-1]:
        score = 0
        current = 1
    else:
        score += 1
        current += 1
        longest = max(longest, current)
print(longest)

