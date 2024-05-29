
def possible_health_configurations(N, S):
    S = sorted(S, reverse=True)
    healths = [0] * (2 ** N)
    healths[0] = S[0]
    for i in range(1, N+1):
        for j in range(2 ** i):
            if healths[j] == 0:
                continue
            if healths[j] < S[j]:
                return "No"
            diff = healths[j] - S[j]
            healths[2*j] = max(healths[2*j], diff)
            healths[2*j + 1] = diff
    return "Yes"

N = 2
S = [4, 2, 3, 1]
print(possible_health_configurations(N, S))
```
