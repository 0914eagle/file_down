
def validate_proof(n, lines):
    assumptions = set()
    
    for i in range(n):
        line = lines[i]
        parts = line.split()
        
        if len(parts) == 2:  # Axiom case
            conclusion = parts[1]
            if conclusion in assumptions:
                assumptions.add(conclusion)
            else:
                return i + 1
        else:  # Inference case
            for assumption in parts[:-2]:
                if assumption not in assumptions:
                    return i + 1
            conclusion = parts[-1]
            assumptions.add(conclusion)
    
    return "correct"

# Input processing
n = int(input())
lines = [input() for _ in range(n)]

# Validate the proof
result = validate_proof(n, lines)
print(result)
```
