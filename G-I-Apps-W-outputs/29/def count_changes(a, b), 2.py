
def count_changes(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))

def max_changes(alt, target):
    return max(count_changes(a, target) for a in alt)

def find_least_incongruous(question, n, alternatives):
    min_changes = float('inf')
    least_incongruous = []
    
    for i in range(n):
        changes = max_changes(alternatives, alternatives[i])
        if changes < min_changes:
            min_changes = changes
            least_incongruous = [alternatives[i]]
        elif changes == min_changes:
            least_incongruous.append(alternatives[i])
    
    return least_incongruous

# Input
question = input().strip()
n = int(input())
alternatives = [input().strip() for _ in range(n)]

# Output
result = find_least_incongruous(question, n, alternatives)
for alt in result:
    print(alt)
```
