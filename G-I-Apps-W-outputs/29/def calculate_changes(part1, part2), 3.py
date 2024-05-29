
def calculate_changes(part1, part2):
    changes = 0
    for p1, p2 in zip(part1, part2):
        if p1 != p2:
            changes += 1
    return changes

def find_least_incongruous_alternatives(question, num_alternatives, alternatives):
    min_incongruousity = float('inf')
    least_incongruous_alternatives = []
    
    for i in range(num_alternatives):
        incongruousity = 0
        for j in range(num_alternatives):
            changes = max(calculate_changes(alt, alternatives[j]) for alt in alternatives[i])
            incongruousity = max(incongruousity, changes)
        
        if incongruousity < min_incongruousity:
            min_incongruousity = incongruousity
            least_incongruous_alternatives = [alternatives[i]]
        elif incongruousity == min_incongruousity:
            least_incongruous_alternatives.append(alternatives[i])
    
    return least_incongruous_alternatives

# Input
question = input()
num_alternatives = int(input())
alternatives = [input().split(', ') for _ in range(num_alternatives)]

# Find and output the least incongruous alternatives
result = find_least_incongruous_alternatives(question, num_alternatives, alternatives)
for alt in result:
    print(', '.join(alt))
```

