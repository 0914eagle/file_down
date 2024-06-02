
def check_AC(N, M):
    if N == M:
        return "Yes"
    else:
        return "No"

# Input
N, M = map(int, input().split())

# Output
print(check_AC(N, M))
