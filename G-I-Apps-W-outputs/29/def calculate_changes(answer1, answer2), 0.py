
def calculate_changes(answer1, answer2):
    changes = 0
    parts1 = answer1.split(', ')
    parts2 = answer2.split(', ')
    for part1, part2 in zip(parts1, parts2):
        if part1 != part2:
            changes += 1
    return changes

def find_least_incongruous_answer(question, alternatives):
    incongruities = {}
    for i in range(len(alternatives)):
        incongruities[i] = max([calculate_changes(alternatives[i], alt) for j, alt in enumerate(alternatives) if j != i])
    
    min_incongruity = min(incongruities.values())
    least_incongruous_answers = [alternative for i, alternative in enumerate(alternatives) if incongruities[i] == min_incongruity]
    
    return least_incongruous_answers

# Input
question = input()
N = int(input())
alternatives = []
for _ in range(N):
    alternatives.append(input())

# Output
least_incongruous_answers = find_least_incongruous_answer(question, alternatives)
for answer in least_incongruous_answers:
    print(answer)
```
