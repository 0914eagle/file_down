

def solve():
    n, m = list(map(int, input().split()))
    species = []
    for i in range(n):
        s, x = input().split()
        s = int(s)
        x = float(x)
        species.append((s, x))

    borders = [0]
    for i in range(1, m):
        borders.append(float('inf'))
    current_section = 1
    replanted = 0
    for s, x in species:
        if s != current_section:
            replanted += 1
            continue
        while x < borders[current_section]:
            current_section += 1
            if current_section > m:
                return replanted
        borders[current_section - 1] = x
        current_section += 1

    return replanted

print(solve())

