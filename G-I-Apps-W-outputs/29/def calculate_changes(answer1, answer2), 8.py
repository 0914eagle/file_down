
def calculate_changes(answer1, answer2):
    changes = 0
    parts1 = answer1.split(", ")
    parts2 = answer2.split(", ")
    for part1, part2 in zip(parts1, parts2):
        if part1 != part2:
            changes += 1
    return changes

def incongruousity(answer, alternatives):
    max_changes = 0
    for alt in alternatives:
        changes = max(calculate_changes(answer, alt), calculate_changes(alt, answer))
        if changes > max_changes:
            max_changes = changes
    return max_changes

def find_least_incongruous(question, num_alternatives, alternatives):
    least_incongruous = []
    min_max_changes = float('inf')
    for alt in alternatives:
        changes = incongruousity(alt, alternatives)
        if changes < min_max_changes:
            min_max_changes = changes
            least_incongruous = [alt]
        elif changes == min_max_changes:
            least_incongruous.append(alt)
    return least_incongruous

# Read input
question = input()
num_alternatives = int(input())
alternatives = []
for _ in range(num_alternatives):
    alternatives.append(input())

# Find least incongruous alternatives
result = find_least_incongruous(question, num_alternatives, alternatives)

# Output result
for answer in result:
    print(answer)
```
