
def check_proof(n, lines):
    assumptions = set()
    valid_lines = set()
    
    for i in range(n):
        line = lines[i].split()
        if len(line) == 2:  # Axiom
            valid_lines.add(i)
        else:
            if all(assumption in valid_lines for assumption in line[:-2]):
                valid_lines.add(i)
            else:
                return i + 1
    
    return "correct"

# Read input
n = int(input())
lines = [input() for _ in range(n)]

# Check proof and print output
print(check_proof(n, lines))
