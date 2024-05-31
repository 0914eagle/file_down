
def generate_names(n):
    names = []
    for i in range(n):
        name = chr(ord('A') + (i % 26)) + 'a' * (i // 26)
        names.append(name)
    return names

def solve_soldiers():
    n, k = map(int, input().split())
    results = input().split()

    names = generate_names(n)

    for i in range(n - k + 1):
        if results[i] == "NO":
            for j in range(k):
                names[i + j] = names[i]

    print(" ".join(names))

solve_soldiers()
