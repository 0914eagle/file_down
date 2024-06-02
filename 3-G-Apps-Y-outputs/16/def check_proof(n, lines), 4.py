
def check_proof(n, lines):
    assumptions = set()
    valid_lines = set()
    
    for i in range(n):
        line = lines[i].split()
        conclusion = line[-1]
        
        if len(line) == 2:  # Axiom
            valid_lines.add(conclusion)
        else:  # Derivation
            line_assumptions = set(line[:-2])
            if line_assumptions.issubset(assumptions):
                valid_lines.add(conclusion)
            else:
                return i + 1
        
        assumptions.add(conclusion)
    
    return "correct"

# Input
n = int(input())
lines = [input() for _ in range(n)]

# Output
print(check_proof(n, lines))
