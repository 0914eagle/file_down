
def count_verdicts(N, verdicts):
    counts = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    
    for verdict in verdicts:
        counts[verdict] += 1
    
    output = []
    for verdict, count in counts.items():
        output.append(f"{verdict} x {count}")
    
    return '\n'.join(output)

# Input
N = int(input())
verdicts = [input() for _ in range(N)]

# Output
print(count_verdicts(N, verdicts))
