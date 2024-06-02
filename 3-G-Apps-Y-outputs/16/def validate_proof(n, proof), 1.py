
def validate_proof(n, proof):
    assumptions = set()
    lines = proof.split('\n')
    
    for i in range(n):
        line = lines[i].split()
        if line[1] == '->':
            conclusion = line[2]
            if len(line) == 3:
                if conclusion not in assumptions:
                    return i + 1
            else:
                for assumption in line[0:-2]:
                    if assumption not in assumptions:
                        return i + 1
            assumptions.add(conclusion)
    
    return 'correct'

# Sample Input
n = 3
proof = " -> ALICE\n -> BOB\n ALICE BOB -> CARL"

print(validate_proof(n, proof))
