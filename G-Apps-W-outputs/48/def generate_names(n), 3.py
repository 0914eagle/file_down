
def generate_names(n):
    names = []
    for i in range(n):
        names.append(chr(65 + i % 26) + ''.join(chr(97 + (i // 26) % 26) for _ in range(min(10, 1 + (i // 26) // 26)))
    return names

def solve():
    n, k = map(int, input().split())
    results = input().split()

    names = generate_names(n)

    for i in range(n - k + 1):
        if results[i] == "NO":
            for j in range(k):
                names[i + j] = "X" * (j + 1)  # Generating arbitrary names for ineffective groups

    print(" ".join(names))

# Input parsing
solve()
