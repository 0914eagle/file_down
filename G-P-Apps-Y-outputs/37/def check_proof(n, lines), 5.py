
def check_proof(n, lines):
    assumptions = set()
    conclusions = set()
    
    for i in range(n):
        line = lines[i].split()
        assumptions_for_line = line[:-2]
        conclusion = line[-1]
        
        if len(assumptions_for_line) > 0:
            if not all(assumption in conclusions for assumption in assumptions_for_line):
                return i + 1
        conclusions.add(conclusion)
    
    return "correct"

n = int(input())
proof_lines = []
for _ in range(n):
    proof_lines.append(input())

result = check_proof(n, proof_lines)
print(result)
```
