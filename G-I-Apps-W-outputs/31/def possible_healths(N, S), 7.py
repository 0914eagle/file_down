
def possible_healths(N, S):
    S.sort()
    # Calculate the possible multiset of healths by simulating the spawning process
    powers_of_two = [2 ** i for i in range(N)]
    possible_healths = []
    for p in powers_of_two:
        for s in range(p):
            possible_healths.append(S[s])
    
    possible_healths.sort()
    
    # Check if the calculated multiset of healths matches the input multiset S
    if possible_healths == S:
        return "Yes"
    else:
        return "No"

# Read input
N = int(input())
S = list(map(int, input().split()))

# Output result
print(possible_healths(N, S))
