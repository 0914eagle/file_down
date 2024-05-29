
def is_possible(N, S):
    S.sort(reverse=True)  # Sort the multiset in descending order
    healths = [S[0]]  # Initialize the health of first slime
    for i in range(N):
        new_healths = [0] * (2 ** (i+1))  # Store the healths of new slimes for this round
        for j in range(2 ** i):
            diff = healths[j] - S[2*j+1]  # Calculate the difference for the next generation
            if diff <= 0 or S.count(healths[j]) < 2:  # Check if next generation is possible
                return "No"
            new_healths[2*j] = healths[j]
            new_healths[2*j+1] = S[2*j]
        healths = new_healths  # Update the healths for the next round
    return "Yes"

# Read input
N = int(input())
S = list(map(int, input().split()))

# Call the function and print the result
print(is_possible(N, S))
```
