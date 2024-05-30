
def check_proof(n, proof_lines):
    conclusions = set()
    for i in range(n):
        line = proof_lines[i]
        assumptions, conclusion = line.split(' -> ')
        
        if all(assumption in conclusions for assumption in assumptions.split()):
            conclusions.add(conclusion)
        else:
            return i + 1
    
    return "correct"

# Read input
n = int(input())
proof_lines = [input() for _ in range(n)]

# Check the proof
result = check_proof(n, proof_lines)
print(result)
```
