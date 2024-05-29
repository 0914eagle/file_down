
def possible_healths(N, S):
    total_slimes = 2 ** N
    S.sort(reverse=True)
    if S[0] != max(S):
        return "No"

    def helper(healths, remaining):
        if not remaining:
            return set(healths) == set(S)

        for i, h in enumerate(S):
            if h in healths:
                continue

            next_healths = healths + [h]
            if helper(next_healths, remaining - 1):
                return True

        return False

    return "Yes" if helper([max(S)], total_slimes - 1) else "No"

# Input parsing
input_data = input().strip().split()
N = int(input_data[0])
S = [int(s) for s in input_data[1:]]

# Check if possible
print(possible_healths(N, S))
```
