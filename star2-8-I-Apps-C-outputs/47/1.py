
def solve(n, m, s, x):
    last_species = [0] * (m + 1)
    for i in range(n):
        if s[i] != last_species[s[i]]:
            last_species[s[i]] = s[i]
        else:
            return 1
    return 0

n, m = map(int, input().split())
s, x = [], []
for _ in range(n):
    si, xi = map(int, input().split())
    s.append(si)
    x.append(xi)

print(solve(n, m, s, x))

