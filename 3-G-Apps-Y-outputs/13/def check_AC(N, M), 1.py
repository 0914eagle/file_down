
def check_AC(N, M):
    if N == M:
        return "Yes"
    else:
        return "No"

# Read input from Standard Input
N, M = map(int, input().split())

# Check if Takahashi's submission gets an AC
result = check_AC(N, M)
print(result)
