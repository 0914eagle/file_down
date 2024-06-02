
def check_proof(n, lines):
    assumptions = set()
    for i in range(n):
        line = lines[i].split()
        if line[0] == '->':
            if line[1] not in assumptions:
                return i + 1
        else:
            if all(assumption in assumptions for assumption in line[:-2]):
                assumptions.add(line[-1])
            else:
                return i + 1
    return 'correct'

# Input
n = int(input())
lines = [input() for _ in range(n)]

# Output
result = check_proof(n, lines)
print(result)
