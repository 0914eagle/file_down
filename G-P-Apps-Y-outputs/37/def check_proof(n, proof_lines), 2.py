
def check_proof(n, proof_lines):
    assumptions = set()
    for i in range(n):
        line = proof_lines[i].split()
        if not line[0]:
            assumptions.add(line[2])
        else:
            if not all(assumption in assumptions for assumption in line[:len(line)-1]):
                return i+1
            assumptions.add(line[len(line)-1])
    return "correct"

n = int(input())
proof_lines = [input() for _ in range(n)]

result = check_proof(n, proof_lines)
print(result)
```
