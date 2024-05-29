
def min_incongruous_answer(question, n, answers):
    def count_changes(answer1, answer2):
        changes = 0
        parts1 = answer1.split(", ")
        parts2 = answer2.split(", ")
        for i in range(len(parts1)):
            if parts1[i] != parts2[i]:
                changes += 1
        return changes

    min_incongruous = float('inf')
    min_incongruous_answers = []

    for answer in answers:
        incongruous = max([count_changes(answer, other) for other in answers])
        if incongruous < min_incongruous:
            min_incongruous = incongruous
            min_incongruous_answers = [answer]
        elif incongruous == min_incongruous:
            min_incongruous_answers.append(answer)

    return min_incongruous_answers

# Input
question = input()
n = int(input())
answers = []
for _ in range(n):
    answers.append(input())

# Output
result = min_incongruous_answer(question, n, answers)
for ans in result:
    print(ans)
```
