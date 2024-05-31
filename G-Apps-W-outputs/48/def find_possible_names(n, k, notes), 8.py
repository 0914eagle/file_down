
def find_possible_names(n, k, notes):
    names = []
    for i in range(n):
        if notes[i] == "YES":
            names.append("A" + "a" * 9)
        else:
            names.append("B" + "b" * 9)
    return names

# Input
n, k = map(int, input().split())
notes = input().split()

# Output
result = find_possible_names(n, k, notes)
print(" ".join(result))
