
def calculate_changes(answer1, answer2):
    changes = 0
    for part1, part2 in zip(answer1, answer2):
        if part1 != part2:
            changes += 1
    return changes

def find_least_incongruous(question, num_alternatives, alternatives):
    incongruities = []
    for i in range(num_alternatives):
        max_changes = 0
        for j in range(num_alternatives):
            if i != j:
                changes = max(calculate_changes(alt.split(", "), alternatives[j].split(", ")) for alt in alternatives[i])
                max_changes = max(max_changes, changes)
        incongruities.append(max_changes)
    
    min_incongruity = min(incongruities)
    least_incongruous = [alternatives[i] for i, incongruity in enumerate(incongruities) if incongruity == min_incongruity]
    return least_incongruous

# Input
question = input()
num_alternatives = int(input())
alternatives = [input().strip() for _ in range(num_alternatives)]

# Output
output = find_least_incongruous(question, num_alternatives, alternatives)
for alt in output:
    print(alt)

# End of code
```
