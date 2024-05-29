
def changes_needed(answer1, answer2):
    changes = 0
    for part1, part2 in zip(answer1, answer2):
        if part1 != part2:
            changes += 1
    return changes

def find_least_incongruous_answer(question, num_answers, answers):
    incongruities = {}
    
    for i in range(num_answers):
        max_changes = 0
        for j in range(num_answers):
            if i != j:
                max_changes = max(max_changes, changes_needed(answers[i], answers[j]))
        incongruities[i] = max_changes
    
    min_incongruity = min(incongruities.values())
    least_incongruous_answers = [answers[i] for i, incongruity in incongruities.items() if incongruity == min_incongruity]
    
    return least_incongruous_answers

# Input
question = input()
num_answers = int(input())
answers = [input().split(", ") for _ in range(num_answers)]

# Output
result = find_least_incongruous_answer(question, num_answers, answers)
for answer in result:
    print(", ".join(answer))
```
