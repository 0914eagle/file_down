
def check_proof(n, proof):
    assumptions = set()
    lines = []
    
    for i in range(n):
        line = proof[i].split()
        if len(line) == 1:  # Axiom
            if line[0] not in assumptions:
                return i + 1
        else:  # Inference rule
            if all(assumption in assumptions for assumption in line[:-1]):
                assumptions.add(line[-1])
            else:
                return i + 1
    
    return "correct"

# Input
n = int(input())
proof = [input() for _ in range(n)]

# Output
result = check_proof(n, proof)
print(result)
