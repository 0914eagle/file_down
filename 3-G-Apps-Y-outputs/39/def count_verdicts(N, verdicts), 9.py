
def count_verdicts(N, verdicts):
    counts = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
    
    for verdict in verdicts:
        counts[verdict] += 1
    
    output = ""
    for verdict, count in counts.items():
        output += f"{verdict} x {count}\n"
    
    return output

# Sample Input
N = 6
verdicts = ["AC", "TLE", "AC", "AC", "WA", "TLE"]

# Output
print(count_verdicts(N, verdicts))
