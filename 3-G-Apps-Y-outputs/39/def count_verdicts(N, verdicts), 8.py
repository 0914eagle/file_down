
def count_verdicts(N, verdicts):
    counts = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
    
    for verdict in verdicts:
        counts[verdict] += 1
    
    print(f"AC x {counts['AC']}")
    print(f"WA x {counts['WA']}")
    print(f"TLE x {counts['TLE']}")
    print(f"RE x {counts['RE']}")

# Read input
N = int(input())
verdicts = [input().strip() for _ in range(N)]

# Call the function with input values
count_verdicts(N, verdicts)
