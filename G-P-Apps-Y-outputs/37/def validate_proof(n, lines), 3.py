
def validate_proof(n, lines):
    assumptions = set()
    for i in range(n):
        line = lines[i].split()
        if line[0] != '->':
            for assumption in line[:-2]:
                if assumption not in assumptions:
                    return i + 1
            assumptions.add(line[-2])
    return 'correct'

# Input reading
n = int(input())
lines = [input() for _ in range(n)]

# Validate the proof
result = validate_proof(n, lines)
print(result)
```
