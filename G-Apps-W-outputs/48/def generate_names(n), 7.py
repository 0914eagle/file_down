
def generate_names(n):
    names = []
    for i in range(n):
        name = chr(65 + i % 26)
        for _ in range(i // 26):
            name += chr(97 + i % 26)
        names.append(name)
    return names

n, k = map(int, input().split())
notes = input().split()

names = generate_names(n)
for i in range(n - k + 1):
    if notes[i] == "NO":
        names[i+k-1] = names[i]

print(" ".join(names))
