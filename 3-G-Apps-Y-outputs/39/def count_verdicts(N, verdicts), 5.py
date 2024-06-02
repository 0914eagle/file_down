
def count_verdicts(N, verdicts):
    counts = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
    
    for verdict in verdicts:
        counts[verdict] += 1
    
    output = ""
    for key, value in counts.items():
        output += f"{key} x {value}\n"
    
    return output

# Input
N = int(input())
verdicts = [input() for _ in range(N)]

# Output
print(count_verdicts(N, verdicts))
