
def validate_proof(n, proof):
    assumptions = set()
    for i in range(n):
        line = proof[i].split()
        conclusion = line[-1]
        if len(line) == 1:  # Axiom
            assumptions.add(conclusion)
        else:  # Inference
            if all(assumption in assumptions for assumption in line[:-2]):
                assumptions.add(conclusion)
            else:
                return i + 1
    return "correct"

# Input
n = int(input())
proof = [input() for _ in range(n)]

# Output
result = validate_proof(n, proof)
print(result)
