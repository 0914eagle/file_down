
def generate_names(n):
    names = []
    for i in range(n):
        name = chr(ord('A') + i % 26)
        name += 'a' * (i // 26)
        names.append(name)
    return names

def solve_effective_group(n, k, notes):
    names = generate_names(n)
    result = []

    for i in range(n - k + 1):
        if notes[i] == 'NO':
            result.extend(names[i:i+k])
        else:
            result.extend(['Xyzzzdj' for _ in range(k)])

    print(' '.join(result))

n, k = map(int, input().split())
notes = input().split()

solve_effective_group(n, k, notes)
