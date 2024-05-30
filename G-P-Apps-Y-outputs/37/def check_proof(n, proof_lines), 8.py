
def check_proof(n, proof_lines):
    assumptions = set()
    for i in range(n):
        line = proof_lines[i].split()
        conclusions = line[1:]
        if not all(conclusion in assumptions for conclusion in conclusions):
            return i + 1
        assumptions.update(conclusions)
    return "correct"

# Read input
n = int(input())
proof_lines = [input() for _ in range(n)]

# Check proof
result = check_proof(n, proof_lines)
print(result)
```
