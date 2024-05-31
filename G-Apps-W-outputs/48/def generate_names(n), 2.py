
def generate_names(n):
    names = []
    for i in range(n):
        name = chr(65 + i)  # Start with uppercase A and increment
        name += "a" * 9  # Add lowercase letters
        names.append(name)
    return names

n, k = map(int, input().split())
notes = input().split()

names = generate_names(n)

for i in range(n - k + 1):
    if notes[i] == "NO":
        names[i+k-1] = names[i]

print(*names)
