
def check_proof(n, proof):
    assumptions = set()
    lines = []

    for i in range(n):
        line = proof[i].split()
        if line[0] != '->':
            assumptions.update(line[:-1])
        else:
            conclusion = line[-1]
            if conclusion not in assumptions:
                return i + 1
            lines.append(conclusion)

    return "correct"

# Input processing
n = int(input())
proof = [input() for _ in range(n)]

# Check the proof
result = check_proof(n, proof)
print(result)
