
def count_verdicts(N, verdicts):
    verdict_counts = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    
    for verdict in verdicts:
        verdict_counts[verdict] += 1
    
    output = []
    for key, value in verdict_counts.items():
        output.append(f"{key} x {value}")
    
    return '\n'.join(output)

# Sample Input
N = 6
verdicts = ['AC', 'TLE', 'AC', 'AC', 'WA', 'TLE']

# Sample Output
print(count_verdicts(N, verdicts))
