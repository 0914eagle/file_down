
def generate_names(n):
    names = []
    for i in range(n):
        name = chr(ord('A') + i)
        name += 'a' * min(9, i)
        names.append(name)
    return names

n, k = map(int, input().split())
results = input().split()

names = generate_names(n)

output = []
for i in range(n - k + 1):
    if results[i] == 'NO':
        for j in range(k):
            output.append(names[i+j])
    else:
        for j in range(k):
            output.append(names[i])

print(' '.join(output))
