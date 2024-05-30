
def check_proof(n, lines):
    assumptions = set()
    for i in range(n):
        line = lines[i].split()
        if not line[0]:
            assumptions.add(line[2])
        else:
            if not all(assumption in assumptions for assumption in line[:len(line)-1]):
                return i + 1
            assumptions.add(line[-1])
    return "correct"

# Read input
n = int(input())
lines = [input() for _ in range(n)]

# Check the proof
result = check_proof(n, lines)
print(result)
```
