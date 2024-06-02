
def check_proof(n, proof):
    assumptions = set()
    lines = []
    
    for i in range(n):
        line = proof[i].split()
        assumptions.update(line[:-1])
        lines.append(line[-1])
        
        if not assumptions.issuperset(line[:-1]):
            return i + 1
    
    return "correct"

# Input
n = int(input())
proof = [input() for _ in range(n)]

# Output
print(check_proof(n, proof))
