
def check_proof(n, proof):
    assumptions = set()
    lines = []
    
    for i in range(n):
        line = proof[i].split()
        conclusion = line[-1]
        if len(line) == 1:  # Axiom
            if conclusion in assumptions:
                assumptions.remove(conclusion)
            else:
                return i + 1
        else:  # Inference
            for assumption in line[:-2]:
                if assumption not in assumptions:
                    return i + 1
            assumptions.add(conclusion)
    
    return "correct"

# Sample Input Parsing
n = int(input())
proof = [input() for _ in range(n)]

# Check the proof
result = check_proof(n, proof)
print(result)
