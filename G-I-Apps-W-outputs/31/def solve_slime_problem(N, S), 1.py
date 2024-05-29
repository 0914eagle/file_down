
def solve_slime_problem(N, S):
    def check_possible(target, curr_s):
        if not target:
            return True
        for i in range(len(curr_s)):
            if curr_s[i] == target[0]:
                new_s = curr_s[:i] + curr_s[i+1:]
                if check_possible(target[1:], new_s):
                    return True
        return False

    S.sort(reverse=True)
    for i in range(N+1):
        healths = [S[0]] * (2**i)
        for j in range(1, 2**i):
            for k in range(len(S)):
                if check_possible([S[k]] * (2**(i-1)), healths[:j]):
                    healths[j] = S[k]
                    S[k] = -1
                    break
        S = [x for x in S if x != -1]

    return "Yes" if not S else "No"

# Sample Input
N = 2
S = [4, 2, 3, 1]
print(solve_slime_problem(N, S))
```
