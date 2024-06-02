
def check_proof(n, proof):
    assumptions = set()
    lines = proof.split('\n')
    
    for i in range(n):
        line = lines[i].split()
        conclusion = line[-1]
        
        if len(line) == 2 and line[0] == '->':
            if conclusion not in assumptions:
                return i + 1
            assumptions.add(conclusion)
        else:
            if not all(assumption in assumptions for assumption in line[:-2]):
                return i + 1
    
    return 'correct'

# Input
n = int(input())
proof = ''
for _ in range(n):
    proof += input() + '\n'

# Output
print(check_proof(n, proof))
