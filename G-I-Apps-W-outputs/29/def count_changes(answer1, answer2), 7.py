
def count_changes(answer1, answer2):
    count = 0
    for part1, part2 in zip(answer1, answer2):
        if part1 != part2:
            count += 1
    return count

def incongruousity(alternative, alternatives):
    max_changes = 0
    for alt in alternatives:
        changes = max(count_changes(alternative, alt), count_changes(alt, alternative))
        if changes > max_changes:
            max_changes = changes
    return max_changes

def find_least_incongruous(question, num_alternatives, alternatives):
    min_incongruousity = float('inf')
    least_incongruous = []

    for i in range(num_alternatives):
        incongruousity_score = incongruousity(alternatives[i], alternatives[:i] + alternatives[i+1:])
        
        if incongruousity_score < min_incongruousity:
            min_incongruousity = incongruousity_score
            least_incongruous = [alternatives[i]]
        elif incongruousity_score == min_incongruousity:
            least_incongruous.append(alternatives[i])
    
    return least_incongruous

question = input().strip()
num_alternatives = int(input().strip())
alternatives = [input().strip().split(", ") for _ in range(num_alternatives)]

result = find_least_incongruous(question, num_alternatives, alternatives)
for ans in result:
    print(", ".join(ans))
```
