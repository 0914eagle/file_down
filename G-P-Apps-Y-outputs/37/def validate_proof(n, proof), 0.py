
def validate_proof(n, proof):
    assumptions = set()
    lines = proof.split('\n')
    
    for i in range(n):
        line = lines[i].split(' ')
        if len(line) == 2:  # Axiom
            if line[1] not in assumptions:
                return i + 1
        else:  # Inference
            if any(assump not in assumptions for assump in line[:-2]):
                return i + 1
            assumptions.add(line[-1])

    return "correct"

# Sample Input
n = 3
proof = 

print(validate_proof(n, proof))
```
