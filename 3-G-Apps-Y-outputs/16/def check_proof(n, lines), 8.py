
def check_proof(n, lines):
    assumptions = set()
    for i in range(n):
        line = lines[i].split()
        conclusion = line[-1]
        if len(line) == 1:  # Axiom
            if conclusion not in assumptions:
                return i + 1
        else:  # Inference
            if not all(assumption in assumptions for assumption in line[:-2]):
                return i + 1
        assumptions.add(conclusion)
    return "correct"

# Read input
n = int(input())
lines = [input() for _ in range(n)]

# Check proof
result = check_proof(n, lines)
print(result)
