
def count_verdicts(N, verdicts):
    verdict_count = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
    
    for verdict in verdicts:
        verdict_count[verdict] += 1
    
    output = ""
    for key, value in verdict_count.items():
        output += f"{key} x {value}\n"
    
    return output

# Input
N = int(input())
verdicts = [input() for _ in range(N)]

# Output
print(count_verdicts(N, verdicts))
