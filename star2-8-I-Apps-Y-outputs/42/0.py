
def solve(s):
    d = dict()
    for line in s:
        if line == "***":
            break
        d[line] = d.get(line, 0) + 1
    max_val = max(d.values())
    if max_val > sum(d.values())/2:
        return list(d.keys())[list(d.values()).index(max_val)]
    return "Runoff!"

print(solve([
    "Penny Franklin",
    "Marti Graham",
    "",
    "",
    "Connie Froggatt",
    "Penny Franklin",
    "Connie Froggatt",
    "Bruce Stanger",
    "Connie Froggatt",
    "Barbara Skinner",
    "Barbara Skinner",
    "***"
]))

