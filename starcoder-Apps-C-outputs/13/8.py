
def input():
    return "wl jkd"

d = dict()

words = ["be", "our", "rum", "will", "dead", "hook", "ship", "blood", "sable", "avenge", "parrot", "captain"]
for w in words:
    for c in w:
        if c not in d:
            d[c] = 0
        d[c] += 1

def solve(s):
    for k in d:
        d[k] = 0
    for c in s:
        if c in d:
            d[c] += 1
    return "".join(sorted(d.keys()))

s = input()
s = s.split(" ")

res = []
for w in s:
    res.append(solve(w))

print(" ".join(res))
